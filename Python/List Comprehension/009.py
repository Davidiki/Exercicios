'''
Dada uma lista de números, use a função map para criar uma nova lista
contendo True para números pares e False para números ímpares.
'''

from random import randint
l = [randint(1,50) for i in range(10)]

l2 = list(map(lambda x: x % 2 == 0, l))

print(f'lista original: {l}\n'
      f'Pares e Impares: {l2}')