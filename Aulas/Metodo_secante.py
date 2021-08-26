"""
Consiste em pegar um ponto 'a' na curva e um ponto 'b' e por meio de
iterações econtrar um ponto 'c' até chegar em y=0.
"""
import numpy as np
import matplotlib.pyplot as plt


# Função utilizada para a atividade.

def f(x):
    return -x ** 2 + 6 * x + 10

def metodo_secante(a, b, epsilon=1e-6):  # r¹=-1,359    /    r²=7,359
    d = 10  # Este "d" serve apenas para iniciar o loop while
    print(epsilon)

    while epsilon <= d:
        d = abs(b - a) / abs(a)
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))  # Forma de econtrar o ponto c
        if abs(c - a) < abs(b - c):  # |c-a| < |b-c| Significa que o ponto "a" está mais perto de "c".
            b, a = a, c

        else:  # |c-a| > |b-c| Significa que o ponto "b" está mais perto de "c".
            a, b = b, c

    print(f'Raiz positiva: {a}')
    return a


k = np.linspace(-4, 10, num=50)

plt.plot(k, f(k), color='firebrick')
plt.plot(metodo_secante(9, 6), 0, 'o', color='crimson')
plt.plot(metodo_secante(2, 3), 0, 'o', color='darkblue')
plt.hlines(0, -5, 11, color='black', linewidth=1)
plt.title('Método da Secante:Isadora & Eric.')

plt.show()
