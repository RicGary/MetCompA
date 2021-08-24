def f(x):
    return 1 / (x ** 2 - 1)


def trapezio(a, b, N):
    delta = (b - a) / N
    I = ((f(a) + f(b)) / 2) * delta

    for i in range(1, N):
        x_i = a + i * delta
        I += f(x_i) * delta

    return I


def erro(a, b, N):
    return abs((trapezio(a, b, N) - trapezio(a, b, N - 1)) / (trapezio(a, b, N)))


print('O valor da integral é: ', trapezio(2, 10, 100))
print('O erro relativo é: ', erro(2, 10, 100))
