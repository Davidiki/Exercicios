'''
Faça um programa em Python que gere uma matriz 10 x 10 de inteiros
aleatórios entre 1 e 50, imprima a matriz e a soma de todos os
elementos de cada linha.
'''
from random import randint

matriz = [0] * 10
somas = []

for i in range(10):
    matriz[i] = [0] * 10
    soma = 0
    for j in range(10):
        matriz[i][j] = randint(1, 50)
        print(f'{matriz[i][j]:02}', end=' ')
        soma += matriz[i][j]
    print()
    somas.append(soma)

print()
print(somas)
