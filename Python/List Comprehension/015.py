'''
Dada uma lista de números, use a função filter para criar uma nova lista
contendo apenas os números ímpares que são menores que 10.
'''
from random import randint

def geraLista():
    return [randint(1,20) for i in range(20)]

def imparMenor5(x):
    return x < 10 and x % 2 != 0

l = geraLista()

l2 = list(filter(imparMenor5, l))

print(l)
print(l2)