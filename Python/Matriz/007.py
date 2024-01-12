'''
Elabore um programa em Python que gere uma matriz 4x6 e calcule e mostre
a sua matriz transposta equivalente.
'''
matriz = [0]*4
print('Matriz gerada')
for i in range(4):
    matriz[i] = [0]*6
    for j in range(6):
        matriz[i][j] = (i*10) + j
        print(f'{matriz[i][j]:02}',end=' ')
    print()
print('\n\nMatriz Transposta')
for i in range(6):
    for j in range(4):
        print(f'{matriz[j][i]:02}',end=' ')
    print()