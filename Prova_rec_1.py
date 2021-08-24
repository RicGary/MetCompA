import numpy as np
import matplotlib.pyplot as plt

# Tarefa 1.a

n = 5
valor = 0

for fila in range(2, n):
    if (n % fila == 0):
        valor += 1

if(valor==0):
    print("É primo.")
else:
    print("Não é primo.")


# Tarefa 1.b

n = int(input("Teste para saber se é primo: "))
valor = 0

for fila in range(2, n):
    if (n % fila == 0):
        valor += 1

if(valor==0):
    print("É primo.")
else:
    print("Não é primo.")


# Tarefa 2.a

def lognormal(x,mu,sigma):
    u , o = mu , sigma

    # Parte da esquerda:
    parte_baixo_e = x*o*(2*np.pi)**(1/2)
    parte_esquerda = 1/parte_baixo_e

    # Parte direita:
    parte_baixo_d = 2*o**2
    parte_cima_d = ((np.log(x))-u)**2
    parte_dividida_d = parte_cima_d/parte_baixo_d
    parte_direita = np.exp(-parte_dividida_d)

    # Resposta:
    P = parte_esquerda*parte_direita

    return P

print(f"Seu valor com x=1, mu=1 e sigma=1 é {lognormal(1,1,1)}.")


# Tarefa 2.b
"""
0 < x < 15      u = 1        σ = 1/2, 1/4, 1/8
Horizontal
lognormal(x,mu,sigma)
"""

x = np.linspace(0,15,num=200)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3)

fig.suptitle('Tarefa 2.b')

ax1.plot(x,lognormal(x,1,1/2),label='σ = 1/2',color='deepskyblue')

ax2.plot(x,lognormal(x,1,1/4),label='σ = 1/4',color='dodgerblue')

ax3.plot(x,lognormal(x,1,1/8),label='σ = 1/8',color='steelblue')

ax1.legend()
ax2.legend()
ax3.legend()

plt.show()


# Tarefa 2.c
"""
0 < x < 15          µ = 0, 1, 2             e σ = 1/4
Vertical
lognormal(x,mu,sigma)
"""

fig, (ax1, ax2, ax3) = plt.subplots(3, 1)

fig.suptitle('Tarefa 2.c')

ax1.plot(x,lognormal(x,0,1/4),label='µ = 0',color='deepskyblue')

ax2.plot(x,lognormal(x,1,1/4),label='µ = 1',color='dodgerblue')

ax3.plot(x,lognormal(x,2,1/4),label='µ = 2',color='steelblue')

ax1.legend()
ax2.legend()
ax3.legend()

plt.show()

