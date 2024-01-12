'''
Defina a função indices_pares que recebe como argumento uma lista de
números inteiros w e devolve a lista dos elementos de w em posições
pares.
'''
from random import randint
def indices_pares(w):
    return [n for n in w[::2]]

l = [randint(1,20) for i in range(20)]
print(l)
print(indices_pares(l))