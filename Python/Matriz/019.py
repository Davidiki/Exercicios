'''
Elabore um programa que leia uma matriz 5x5 e mostre os elementos do
triângulo superior esquerdo da matriz (elementos acima da diagonal
secundária).
'''

M = [0]*5
print('Matri gerada')
for i in range(5):
    M[i] = [0]*5
    for j in range(5):
        M[i][j] = (i*10)+j
        print(f'{M[i][j]:02}',end=' ')
    print()

print('\nTriângulo superior esquerdo')
for i in range(5):
    for j in range(5):
        if i + j <= 3:
            print(f'{M[i][j]:02}',end=' ')
        else:
            print('  ',end=' ')
    print()