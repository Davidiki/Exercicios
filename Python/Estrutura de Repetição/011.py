'''
Escreva um programa que gere um conjunto de 20 números inteiros
aleatórios entre 1 e 50 e mostre qual foi o maior e o menor valor gerado.
'''

from random import randint

cont = 1
maior = 0
menor = 50

while cont <= 20:
    num = randint(1, 50)
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    print(num,end=' ')
    cont += 1
print(f'\n\nMaior número gerado: {maior}\n'
      f'Menor número gerado: {menor}')