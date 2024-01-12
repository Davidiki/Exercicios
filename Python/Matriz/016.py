'''
Elabore um programa que leia uma matriz 5x5 e calcule e mostre a
diagonal secundária.
'''


matriz = [0]*5
for i in range(5):
    matriz[i] =  [0]*5
    for j in range(5):
        matriz[i][j] = (i*10) + j
        print(f'{matriz[i][j]:02}',end=' ')
    print()

print('\nDiagonal pricipal')
for i in range(5):
    for j in range(5):
        if i == j:
            print(f'{matriz[i][j]:02}',end=' ')
        else:
            print('  ',end=' ')
    print()