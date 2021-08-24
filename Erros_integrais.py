'''
Trapézio

1) Escreva um programa que calcule o erro do método do trapézio em
função de N. Este programa deve fazer o N variar entre 1 e um certo N
máximo (considere Nmax=100). Para cada valor de N, calcule quanto vale a
integrar e guarde este valor em uma lista ou array int_trap[N]. Assim, você
poderá calcular o erro relativo
erro_trap[N] = (int_trap[N]-int_trap[N-1])/int_trap[N]

2) Considere a função a ser integrada f(x)= 1/(x2-1) e o intervalo de
integração de x=2 a x=10. Faça um gráfico de int_trap[N] vs N e
erro_trap[N] vs N.

Simpons

1) Escreva um programa que calcule o erro do método de Simpson em
função de N de maneira similar ao do exercício do método do trapézio.
Lembre que o método de Simpson requer que N seja par.

2) Considere a função a ser integrada f(x)= 1/(x2-1) e o intervalo de
integração de x=2 a x=10. Faça um gráfico de int_simpson[N] vs N e
erro_simpson[N] vs N.

3) Faça um mini-relatório em Latex incluindo:
a) Os códigos desenvolvidos (use o comando verbatim)
b) Os gráficos gerados

4) Envie o pdf do mini-relatório pelo Moodle
'''
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

def erro(N,a,b):
    erro = abs(trapezio(N,a,b)-trapezio(N-1,a,b))/trapezio(N,a,b)
    return erro

x = []  # Valor de x = N
for N in range(1,101):
    x.append(N)

y = []  # Valor de y = Integral(N)
for N in range(1,101):
    y.append(trapezio(N,2,10))

y_erro = [1]
for N in range(2,101):
    y_erro.append(erro(N,2,10))


plt.plot(x,y,color='teal',label='Integral(N)')
plt.xlabel('N')
plt.ylabel('Integral(N)')
plt.title('Comparando valores de N: Método Trapézio.')

plt.scatter(x,y_erro,color='crimson',label='Erro',marker='.')

plt.legend()
plt.show()

#######################################################################################################################

def Simpson(N, a, b):  # N precisa ser par, 2N.

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

def erro2(N,a,b):
    erro2 = abs(Simpson(N,a,b)-Simpson(N-1,a,b))/Simpson(N,a,b)
    return erro2

x2 = []  # Valor de x = N
for N in range(2,101,2):
    x2.append(N)

y2 = []  # Valor de y = Integral(N)
for N in range(1,51):
    y2.append(Simpson(N,2,10))

y_erro2 = [1]
for N in range(2,51):
    y_erro2.append(erro2(N,2,10))


plt.plot(x2,y2,color='teal',label='Integral(N)')
plt.xlabel('N')
plt.ylabel('Integral(N)')
plt.title('Comparando valores de N: Método Simpson.')
plt.scatter(x2,y_erro2,color='crimson',label='Erro',marker='.')

plt.legend()
plt.show()

#######################################################################################################################
plt.plot(x,y,color='teal',label='Integral(N): Trapézio')
plt.plot(x2,y2,color='darkturquoise',label='Integral(N): Simpson')


plt.scatter(x2,y_erro2,color='orangered',label='Erro: Simpson',marker='.')
plt.scatter(x,y_erro,color='maroon',label='Erro: Trapézio',marker='.')

plt.title('Comparando Métodos.')
plt.xlabel('N')
plt.ylabel('Integral(N)')
plt.legend()
plt.show()


