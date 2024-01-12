'''
Elabore um algoritmo que leia uma matriz 5x5 e verifique se ela é ou
não uma matriz identidade.  Uma matriz é identidade se todos os
elementos da diagonal principal são 1s e os demais 0s.
'''

from random import randint
M = [0] * 5

for i in range(5):
    M[i] = [0] * 5
    for j in range(5):
        if i == j:
            M[i][j] = randint(0,1)
        else:
            M[i][j] = randint(0,1)
        print(f'{M[i][j]}', end=' ')
    print()

identidade = True
for i in range(5):
    for j in range(5):
        if i == j and M[i][j] != 1:
            identidade = False
        elif i != j and M[i][j] != 0:
            identidade = False

# Imprimir o resultado
if identidade:
    print("\nA matriz é uma matriz identidade.")
else:
    print("\nA matriz não é uma matriz identidade.")
