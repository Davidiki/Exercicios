'''
Elabore um programa que leia uma matriz 5x5 e mostre os elementos do
triângulo inferior direito da matriz (elementos abaixo da diagonal
secundária).
'''

M = [0]*5
print('Matriz Gerada')
for i in range(5):
    M[i] = [0]*5
    for j in range(5):
        M[i][j] = (i*10)+j
        print(f'{M[i][j]:02}',end=' ')
    print()


print('\nTriângulo inferior direito da matriz')
for i in range(5):
    for j in range(5):
        if i+j >= 5:
            print(f'{M[i][j]:02}',end=' ')
        else:
            print('  ',end=' ')
    print()