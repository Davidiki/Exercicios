'''
Faça um programa em Python que gere uma matriz M[10][10] com números
aleatórios de 1 a 50 e copie para um vetor de 10 elementos, os números
da diagonal principal. Imprima a matriz e o vetor.
'''

from random import randint
M = [0]*10
V = []
for i in range(10):
    M[i] = [0]*10
    for j in range(10):
        M[i][j] = randint(1,50)
        print(f'{M[i][j]:02}',end=' ')
    print()

for i in range(10):
    for j in range(10):
        if i == j:
            V.append(M[i][j])

print(f'\n\nValores da Diagonal principal\n{V}')