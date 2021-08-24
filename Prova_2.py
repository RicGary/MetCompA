import numpy as np
import matplotlib.pyplot as plt


def f(x, u):
    return 1 / (np.exp((x - u) / 0.02) + 1)


def g(u):
    return Simpson(u) - 1


def Simpson(u, N=50, a=0, b=2):  # N precisa ser par, 2N.

    h = (b - a) / (2 * N)
    f_a = f(a, u)
    f_b = f(b, u)

    par = 0
    impar = 0
    for i in range(2, 2 * N, 2):  # Par
        par += f(a + i * h, u)

    for i in range(1, 2 * N, 2):  # Impar
        impar += f(a + i * h, u)

    integral = (h / 3) * (f_a + f_b + 4 * impar + 2 * par)
    return integral


def metodo_secante(a, b, epsilon=1e-6):  # r¹=-1,359    /    r²=7,359
    d = 10  # Este "d" serve apenas para iniciar o loop while

    while epsilon <= d:
        d = abs(b - a) / abs(a)
        c = (a * g(b) - b * g(a)) / (g(b) - g(a))  # Forma de econtrar o ponto c
        if abs(c - a) < abs(b - c):  # |c-a| < |b-c| Significa que o ponto "a" está mais perto de "c".
            b, a = a, c

        else:  # |c-a| > |b-c| Significa que o ponto "b" está mais perto de "c".
            a, b = b, c

    print(f'Raiz positiva: {a}')
    return a


# método alternativo mais simples?? Não precisa do método da secante

u = 0

for _ in range(20):
    u += 0.1
    gu = Simpson(u) - 1
    if gu == 0:
        print(round(u, 4))


def gx(x):
    return 1 / (np.exp((x - 1) / 0.02) + 1)

metodo_secante(0,2)

x = np.linspace(0, 2, num=200)
plt.plot(x, gx(x), color="crimson")
plt.title("Distribuição de Fermi-Dirac. u = 1.")
plt.xlabel("x")
plt.ylabel("Energia")
plt.legend()
plt.show()
