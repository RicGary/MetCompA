'''
                                  ╔═══════════════════════════════════╗
                                  ║Acrescentar função derivadas Gerais║
                                  ╚═══════════════════════════════════╝
Definir derivadas ordem maior que 1.De

                                     ┌———————————————————————————┐
                                     │Forma correta porém depende│
                                     └———————————————————————————┘

-=Ela não retorna o valor 100% correto da derivada=-

'''

'''
def f(x):  #5x^2-3x
    return 5*x**2-3*x
#Parte 1


def f_linha(x, delta_x):
    return (f(x+delta_x) - f(x))/delta_x



print(f_linha(1 ,1e-2))     #7.050000000000001
print(f_linha(1 ,1e-4))     #7.000499999998411
print(f_linha(1 ,1e-6))     #7.00000500053477
print(f_linha(1 ,1e-8))     #razoável   =   6.999999957457703
print(f_linha(1 ,1e-10))    #razoável   =   7.000000579182597
print(f_linha(1 ,1e-12))    #7.000622304076387
print(f_linha(1 ,1e-14))    #6.927791673660977
print(f_linha(1 ,1e-16))    #1e-16 = 0 pois  em float o máximo de casas pós virg. é 15.     =       0
print('_______________')
print(f_linha(1 ,1e-9))     #7.000000579182597
'''

'''
                              ╔═══════════════════════════════════════════╗
                              ║Forma correta com arredondamento de 4 casas║
                              ╚═══════════════════════════════════════════╝
-=É uma aproximação=-
'''

'''
pergunta = input('Função para derivar: ')
def f(x):
    expressao = eval(pergunta)
    return expressao

def f_linha(x, delta_x):        #calcular derivada com precisão arredondada
    resposta_derivada = ((f(x + delta_x) - f(x)) / delta_x)
    print((round(resposta_derivada,4)))
    return resposta_derivada

f_linha(1 ,1e-8)     #razoável   =   6.999999957457703
f_linha(1 ,1e-10)    #razoável   =   7.000000579182597 // 1e-10 = 1e-9

#Valores de delta_x entre 1e-2 até 1e-6 possuem uma precisão duvidável, maior que 1e-10 precisão cai
#1e-16 = 0 pois  em float o máximo de casas pós virg. é 15.     =       0

'''

'''
                                    ╔══════════════════════════════════════╗
                                    ║Derivada à direita central e seu erro.║
                                    ╚══════════════════════════════════════╝
                                    
'''
import numpy as np

print('Função para o trabalho: x**3*(np.sin(x))')        #f(x)= x3 sen(x)  //  3sin(x)+cos(x)
pergunta = input('Função para derivar: ')
def f(x):
    expressao = eval(pergunta)
    return expressao

def f_linha(x, delta_x):        #calcular derivada com precisão arredondada

    #derivada à direita
    derivada_direita = ((f(x + delta_x) - f(x)) / delta_x)
    print(derivada_direita)

    #derivada centra
    derivada_central = (f(x+delta_x)-f(x-delta_x))/(2*delta_x)
    print(derivada_central)

    erro = (3*np.sin(x)+np.cos(x) - derivada_central)/derivada_central
    print(erro)

    return derivada_direita, derivada_central , erro

f_linha(1 ,1e-10)    #razoável   =   7.000000579182597 // 1e-10 = 1e-9