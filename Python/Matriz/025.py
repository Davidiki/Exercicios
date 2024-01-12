'''
Elabore um algoritmo para gerar a seguinte matriz 5x5:
'''

M = [0]*5
for i in range(5):
    M[i] = [0]*5
    for j in range(5):
        if i == j or i + j == 4:
            M[i][j] = 1
        else:
            M[i][j] = 0
        print(f'{M[i][j]}',end=' ')
    print()