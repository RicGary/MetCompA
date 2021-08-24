"""
Calculo aproximado da integral utilizando o método do trapézio.
Consiste em dividir a área abaixo da curva em pequenos quadrados e trapézios
e fazer a soma.
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes as ax

def f(x):
    # return 1 / (x ** 2 - 1)
    return 1 / (x ** 2 - 1)


def trapezio(N, a, b):  # A = (B+b)h/2
    delta_x = (b - a) / N
    A = 0
    x = a

    for i in range(a,N+1):
        base1 = f(x)    # ponto a
        x += delta_x
        base2 = f(x)    # ponto b
        if base1 >= base2:
            B = base1
            b = base2
        if base1 <= base2:
            B = base2
            b = base1

        A += ((B+b)*delta_x)/2
    return A

print(trapezio(100,2,10))