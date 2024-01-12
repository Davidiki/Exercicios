'''
Elabore um programa em Python que leia duas matrizes A (mxn) e B (pxq)
e calcule e mostre a matriz Python que é a soma de A com B (caso a soma
seja possível).
'''

from random import randint
print('Dimensões da matriz A')
m = int(input('Quantidade de linhas: '))
n = int(input('Quantidade de colunas: '))

print('\nnDimensões da matriz B')
p = int(input('Quantiade de linhas: '))
q = int(input('Quantidade de colunas: '))


if m == p and n == q:
    print('\nMatriz A')
    a = [0]*m
    for i in range(m):
        a[i] = [0]*n
        for j in range(n):
            a[i][j] = randint(1, 50)
            print(f'{a[i][j]:02}', end=' ')
        print()

    print('\nMatriz B')
    b = [0]*p
    for i in range(p):
        b[i] = [0]*q
        for j in range(q):
            b[i][j] = randint(1,50)
            print(f'{b[i][j]:02}',end=' ')
        print()

    c = [0]*m
    print('\nMatriz C')
    for i in range(m):
        c[i] = [0]*n
        for j in range(n):
            c[i][j] = a[i][j] + b[i][j]
            print(f'{c[i][j]:02}',end=' ')
        print()
else:
    print('\nNão é possível somar matrizes com dimensões diferentes')