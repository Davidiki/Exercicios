'''
Dada uma lista de números, use a função filter para criar uma nova lista
contendo apenas os números pares.
'''
from random import randint
def geraLista():
    return [randint(1,50) for i in range(10)]

def par(x):
    return x % 2 == 0

num = geraLista()
numPar = list(filter(par, num))
print(f'{num}\n'
      f'{(numPar)}')