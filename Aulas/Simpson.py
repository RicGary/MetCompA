"""
Aplicando método de Simpson para:

1-) Implemente uma função em Python que calcule uma integral utilizando o
método de Simpson. Esta função deve:
a) Receber como entrada uma função, os limites do intervalo de integração (a,b)
e o número de 'fatias' N
b) Retornar o valor da integral

2-) Utilize o método de Simpson para calcular a integral da função
f(x)=x^5+3x+5 no intervalo [0,1] com N=10. Aumente o valor de N para 100
e depois 1000 e veja como o resultado muda. Compare com os resultados
obtidos na última aula com o método do trapézio.
"""


def f(x):
    # return 1 / (x ** 2 - 1)
    return 1 / (x ** 2 - 1)


def Simpson(f, N, a, b):  # N precisa ser par, 2N.

    h = (b - a) / (2 * N)

    f_a = f(a)
    f_b = f(b)

    par = 0
    impar = 0
    for i in range(2, 2 * N, 2):  # Par
        par += f(a + i * h)

    for i in range(1, 2 * N, 2):  # Impar
        impar += f(a + i * h)

    integral = (h / 3) * (f_a + f_b + 4 * impar + 2 * par)

    return integral


print(Simpson(f,50,2,10))
