"""
                                    ╔═══════════════════════════════════════╗
                                    ║Derivadas centrais à direita e seu erro║
                                    ╚═══════════════════════════════════════╝
"""

import matplotlib.pyplot as plt
import numpy as np


# print('Função para o trabalho: x**3*(np.sin(x))')        #f(x)= x3 sen(x)  //  3sin(x)+cos(x)
# pergunta = input('Função para derivar: ')
# def f(x):
#    expressao = eval(pergunta)
#    return expressao

def f(x):
    expressao = x ** 3 * (np.sin(x))
    return expressao


def f_analitica(x):
    expressao = (3 * x ** 2 * np.sin(x) + x ** 3 * np.cos(x))
    return expressao


def f_linha_dir(x, delta_x):  # calcular derivada com precisão arredondada

    # derivada à direita
    derivada_direita = ((f(x + delta_x) - f(x)) / delta_x)
    # print(derivada_direita)

    return derivada_direita


def f_linha_cent(x, delta_x):
    # derivada central
    derivada_central = (f(x + delta_x) - f(x - delta_x)) / (2 * delta_x)
    # print(derivada_central)

    return derivada_central


def erro_f_cent(x, delta_x):
    parte_cima_positivo = ((f_analitica(x)) - (f_linha_cent(x, delta_x))) ** 2
    parte_baixo_positivo = (f_analitica(x)) ** 2
    erro = (parte_cima_positivo ** 0.5) / (parte_baixo_positivo ** 0.5)

    return erro


def erro_f_dir(x, delta_x):
    parte_cima_positivo = ((f_analitica(x)) - (f_linha_dir(x, delta_x))) ** 2
    parte_baixo_positivo = (f_analitica(x)) ** 2
    erro = (parte_cima_positivo ** 0.5) / (parte_baixo_positivo ** 0.5)

    return erro


# print('Derivada à direita: ',f_linha_dir(1,1e-10))
# print('Derivada central: ',f_linha_cent(1,1e-10))
# print('Erro derivada à direita: ',erro_f_dir(1,1e-10))
# print('Erro derivada central: ',erro_f_cent(1,1e-10))

# Usar subfigure

d_x = np.logspace(-16, 0, num=100)
graf_direita = f_linha_dir(3, d_x)
graf_centro = f_linha_cent(3, d_x)
graf_erro_dir = erro_f_dir(3, d_x)
graf_erro_cent = erro_f_cent(3, d_x)

plt.plot(d_x, graf_direita, label="f'numérico à direita.", color='red')
plt.plot(d_x, graf_centro, label="f'numérico central.", color='blue')

plt.hlines(-22.919557, 1, 1e-16, label='Valor analítico', color='purple', linestyles='--')
plt.legend()
plt.ylabel('f \'(x)')
plt.xlabel('\u0394x')
plt.title('Análise de derivadas:Valores.')
plt.xscale('log')

plt.show()

plt.plot(d_x, graf_erro_dir, label="Erro f' direita.", color='red')
plt.plot(d_x, graf_erro_cent, label="Erro f' centro.", color='black')
plt.legend()
plt.ylabel('Erro')
plt.xlabel('\u0394x')
plt.title('Análise de derivadas:Erros.')
plt.xscale('log')
plt.yscale('log')

plt.show()

'''
d_x = np.logspace(-16, 0, num=100)
graf_direita = f_linha_dir(3, d_x)
graf_centro = f_linha_cent(3, d_x)
graf_erro_dir = erro_f_dir(3, d_x)
graf_erro_cent = erro_f_cent(3, d_x)

fig, axs = plt.subplots(2)
fig.suptitle('Análise de derivada.')
axs[0].plot(d_x, graf_direita, label="f'numérico à direita.", color='red')
axs[1].plot(d_x, graf_erro_dir, label="Erro f' direita.", color='red')

plt.show()
'''
