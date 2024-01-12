'''
Elabore um algoritmo para gerar a seguinte matriz 5x5
0 0 0 0 0
0 1 2 3 4
0 2 4 6 8
0 3 6 9 12
0 4 8 12 16
'''

M = [0]*5
for i in range(5):
    M[i] = [0]*5
    for j in range(5):
        M[i][j] = i*j
        print(f'{M[i][j]}',end=' ')
    print()
