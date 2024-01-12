'''
Faça um programa que leia 10 inteiros e imprima sua média.
'''
from random import randint

soma = 0
for i in range(1,11):
    num = randint(1,100)
    print(num, end=' ')
    soma += num

media = soma / 10
print(f'Média: {media}')