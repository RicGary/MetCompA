"""
Atividade consiste em utilizar o método da secante para descobrir qual o valor
de theta para que o objeto chegue ao ponto proposto pela atividade.
"""
import numpy as np
import matplotlib.pyplot as plt

# g = 9.98 m/s2
# yo = 1 m
# x = 50 m
# vo = 100 km/h

'''
expressao = x - (v*np.cos(teta)/g)*v*np.sen(teta)+(v**2*np.sen(teta)**2+2*g*y)**0.5
'''


def f(teta, g=9.98, y=1, x=50, v=100/3.6):
    return x - ((v * np.cos(teta) / 9.98) * (v * np.sin(teta) + np.sqrt((v**2) * ((np.sin(teta))**2) + 2 * 9.98 * y)))


def trajetoria(a, b, epsilon=1e-12):
    d = 10
    while epsilon <= d:
        d = abs(b - a) / abs(a)
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))  # Forma de econtrar o ponto c
        if abs(c - a) < abs(b - c):  # |c-a| < |b-c| Significa que o ponto "a" está mais perto de "c".
            b, a = a, c

        else:  # |c-a| > |b-c| Significa que o ponto "b" está mais perto de "c".
            a, b = b, c

    print(f'Raiz positiva: {a}')
    return a

trajetoria(0.2, 0.6)

trajetoria(0.6, 1.4)

print(f(0.328))
