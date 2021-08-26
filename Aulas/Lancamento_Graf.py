"""
Atividade consiste em utilizar o método da secante para descobrir qual o valor
de theta para que o objeto chegue ao ponto proposto pela atividade.
Aqui está o gráfico.
"""

import numpy as np
import matplotlib.pyplot as plt


def t1(y=1, v=100 / 3.6, g=9.98):
    return (1 / g) * (v * np.sin(0.328579) + (v ** 2 * np.sin(0.328579) ** 2 + 2 * g * y) ** 0.5)


def t2(y=1, v=100 / 3.6, g=9.98):
    return (1 / g) * (v * np.sin(1.222219) + (v ** 2 * np.sin(1.222219) ** 2 + 2 * g * y) ** 0.5)


def x1(t, v=100 / 3.6, teta=0.328579):
    return v * np.cos(teta) * t


def x2(t, v=100 / 3.6, teta=1.222219):
    return v * np.cos(teta) * t


def y1(t, y=1, v=100 / 3.6, teta=0.328579, g=9.98):
    return y + v * np.sin(teta) * t - 0.5 * g * t ** 2


def y2(t, y=1, v=100 / 3.6, teta=1.222219, g=9.98):
    return y + v * np.sin(teta) * t - 0.5 * g * t ** 2


def f(teta, x=50, y0=1, v0=100 / 3.6):
    return x - ((v0 * np.cos(teta) / 9.98) * (
            v0 * np.sin(teta) + np.sqrt((v0 ** 2) * ((np.sin(teta)) ** 2) + 2 * 9.98 * y0)))


def metodo_secante(a, b, epsilon=1e-12):
    d = 10 * epsilon
    while epsilon <= d:
        d = abs(b - a) / abs(a)
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if abs(c - a) < abs(b - c):
            b, a = a, c

        else:
            a, b = b, c

    print(f'raíz: {a}')
    return a


theta = np.linspace(0, 1.5, num=50)
f_ponto = f(theta, 50, 1, 27.7778)

plt.plot(theta, f_ponto, label='', markersize='3', c='k')
plt.plot(metodo_secante(0.2, 0.6), 0, 'o', color='crimson')
plt.plot(metodo_secante(0.6, 1.4), 0, 'o', color='darkblue')
plt.hlines(0, 0, 1.6, color='#c8c8cc', ls='--')
plt.xlabel(r'${\theta}$', fontsize=14)
plt.ylabel(r"$f({\theta})$", fontsize=14)
plt.title('Método da Secante')

plt.show()

t1 = np.linspace(0, 5.269933198047317, num=50)
t2 = np.linspace(0, 1.901739126624874, num=50)

plt.plot(x1(t2), y1(t2), color='crimson', label=r'${\theta}$ = 18,82°')
plt.plot(x2(t1), y2(t1), color='darkorange', label=r'${\theta}$ = 70,02°')
plt.xlabel('x(t)', fontsize=14)
plt.ylabel('y(t)', fontsize=14)
plt.title('Trajetória do projétil')
plt.legend()

plt.show()
