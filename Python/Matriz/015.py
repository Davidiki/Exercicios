'''
Elabore um programa em Python que gere uma matriz aleatória (9x9), com
números entre 0 e 10, imprima-a. Após, peça o quadrante desejado e
imprima os elementos desse quadrante.
'''

from random import randint
matriz = [0]*9

print("\nNúmeros gerados")
for i in range(9):
    matriz[i] = [0]*9
    for j in range(9):
        matriz[i][j] = randint(0,10)
        print(f'[{matriz[i][j]:02}]',end=' ')
    print()

quadrante = int(input("Informe o quadrante -> "))
if quadrante == 1:
    for i in range(0,3):
        for j in range(0,3):
            print(f'[{matriz[i][j]:02}]',end=' ')
        print()
elif quadrante == 2:
    for i in range(0,3):
        for j in range(5,9):
            print(f'[{matriz[i][j]:02}] ',end=' ')
        print()
elif quadrante == 3:
    for i in range(5,9):
        for j in range(0,3):
            print(f'[{matriz[i][j]:02}]',end=' ')
        print()
elif quadrante == 4:
    for i in range(5,9):
        for j in range(5,9):
            print(f'[{matriz[i][j]:02}]',end=' ')
        print()
else:
    print("Quadrante inválido!!")