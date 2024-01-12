'''
Dada uma lista de números, use a função map para criar uma nova lista
que contenha o dobro de cada número da lista original.
'''

from random import randint


lista = [randint(1,50) for i in range(10)]
dobro = map(lambda x: x*2, lista)
print(f'Lista original: {lista}\n'
      f'Dobro: {list(dobro)}')