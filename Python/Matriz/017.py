'''
Elabore um programa que leia uma matriz 5x5 e mostre os elementos do
triângulo superior direito da matriz (elementos acima da diagonal
principal).
'''

matriz = [0]*5
for i in range(5):
    matriz[i] = [0]*5
    for j in range(5):
        matriz[i][j] = (i*10) + j
        print(f'{matriz[i][j]:02}',end=' ')
    print()
print()

for i in range(5):
    for j in range(5):
        if j > i:
            print(f'{matriz[i][j]:02}', end=' ')
        else:
            print('  ', end=' ')  # Dois espaços para manter o formato
    print()