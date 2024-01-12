'''
Elabore um programa que leia uma matriz 4x6 e calcule e mostre a sua
matriz transposta equivalente.
'''

M = [0]*4
print('Matriz gerada')
for i in range(4):
    M[i] = [0]*6
    for j in range(6):
        M[i][j] = (i*10)+j
        print(f'{M[i][j]:02}',end=' ')
    print()

print('\nMatriz transposta')
for i in range(6):
    for j in range(4):
        print(f'{M[j][i]:02}',end=' ')
    print()

