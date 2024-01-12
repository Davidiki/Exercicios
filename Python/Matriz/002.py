'''
Faça um programa em Python que gere uma matriz 10 x 10 de inteiros
aleatórios entre 1 e 50, imprima a matriz e a média de todos os
elementos.
'''

from random import randint

matriz = [0]*10
soma = 0

for i in range(10):
    matriz[i] = [0] * 10
    for j in range(10):
        matriz[i][j] = randint(1,50)
        print(f'{matriz[i][j]:02}',end=' ')
        soma += matriz[i][j]
    print()

media = soma / len(matriz*10)

print(f'\nA média dos valores matriz é: {media}')

