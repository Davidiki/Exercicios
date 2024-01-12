'''
Defina a função prod_lista que recebe como argumento uma lista de números
inteiros e devolve o produto dos seus elementos.
'''
from random import randint
from operator import mul
from functools import reduce
def prod_lista(lista):
    return reduce(mul, lista)

l = [randint(1,5) for i in range(5)]
print(f'Elemetos: {l}\n'
      f'Soma dos elementos: {prod_lista(l)}')
