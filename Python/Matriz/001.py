'''
Faça um programa em Python que leia uma matriz 2 x 3 de inteiros,
imprima a matriz e a soma de todos os elementos.
'''

from random import randint
linhas = int(input('Digite a quantidade de linhas: '))
colunas = int(input('Digite a quantidade de colunas: '))

matriz = [0] * linhas
soma = 0

print('\nElementos da matriz\n')

for i in range(linhas):
    matriz[i] = [0] * colunas
    for j in range(colunas):
        matriz[i][j] = (i*10) + j
        print(f'{matriz[i][j]:02}',end=' ')
        soma += matriz[i][j]
    print()

print(f'a soma da matriz é: {soma}')
