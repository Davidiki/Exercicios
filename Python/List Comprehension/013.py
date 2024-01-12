'''
Dada uma lista de números, use a função filter para criar uma nova lista
contendo apenas os números positivos.
'''

from random import randint
def geraLista():
    return [randint(-50,50) for i in range(20)]

def numPositivo(n):
    return n >= 0

l = geraLista()
l2 = list(filter(numPositivo, l))

print(l)
print(l2)