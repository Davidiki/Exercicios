'''
Escreva um programa em Python que gere uma matriz M[10][10] com números
aleatórios de 1 a 50, peça um número de uma linha qualquer, entre 0 e 9,
e copie os elementos dessa linha para um vetor. Imprima a matriz e o
vetor.
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

num = int(input('\nDigite o número da linha que você deseja saber os valores: '))
for i in range(10):
    V.append(M[num][i])

print(V)