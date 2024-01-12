'''
Faça um programa em Python que gere uma matriz 10 x 10 de inteiros
entre 1 e 50, imprima a matriz e o menor elemento de cada linha.
'''

from random import randint

matriz = [0]*10
menores = []

for i in range(10):
    matriz[i] = [0]*10
    menor = 50
    for j in range(10):
        matriz[i][j] = randint(1,50)
        print(f'{matriz[i][j]:02}',end=' ')
        if matriz[i][j] < menor:
            menor = matriz[i][j]
    menores.append(menor)
    print()


print(f'\nMenor número de cada linha {menores}')