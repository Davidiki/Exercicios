'''
Escreva um programa em Python que gere uma matriz M[5][5], com números
aleatórios entre 1 e 50. Imprima a matriz. A seguir, troque os elementos
da diagonal principal com os elementos da diagonal secundária. Imprima a
nova matriz.
'''

from random import randint

M = [0]*5
print('Matriz antes da mudança')
for i in range(5):
    M[i] = [0]*5
    for j in range(5):
        M[i][j] = randint(1,50)
        print(f'{M[i][j]:02}',end=' ')
    print()

print('\nMatriz após a mudança')
for i in range(5):
    for j in range(5):
        if i == j:
            M[i][j], M[i][4-i] = M[i][4-i], M[i][j]

for i in range(5):
    for j in range(5):
        print(f'{M[i][j]:02}',end=' ')
    print()