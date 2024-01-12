'''
Faça um programa em Python que gere uma matriz 10 x 10 de inteiros
entre 1 e 50, imprima a matriz e o menor elemento de cada coluna.
'''

from random import randint

print("Matriz gerada")
matriz = [0] * 10
for i in range(10):
    matriz[i] = [0] * 10
    for j in range(10):
        matriz[i][j] = randint(1,50)
        print(f"{matriz[i][j]:02}",end=" ")
    print()

print("\nMenor de cada coluna:",end=' ')
for i in range(10):
    menor = matriz[0][i]
    for j in range(10):
        if matriz[j][i] < menor:
            menor = matriz[j][i]
    print(f"{menor:02}",end=" ")