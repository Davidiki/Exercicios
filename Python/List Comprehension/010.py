'''
Dada uma lista de números, use a função map para criar uma nova lista
onde cada número é somado a uma constante (por exemplo, 5).
'''
from random import randint
num = int(input('Digite o número a ser somado: '))
l = [randint(1,50) for i in range(10)]
l2 = list(map(lambda x: x+num, l))

print(f'Lista gerada: {l}\n'
      f'Lista somada à {num}: {l2}')