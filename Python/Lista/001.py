'''
Leia um vetor de 10 números inteiros e calcule e mostre o maior e o
menor elementos do vetor.
'''

from random import randint

a = []
maior = 0
menor = 51
for i in range(10):
    a.append(randint(1, 50))
    if a[i] <= menor:
        menor = a[i]
    if a[i] >= maior:
        maior = a[i]
print(f'Vetor: {a}\n'
      f'Maior valor: {maior}\n'
      f'Menor valor: {menor}')