'''
Elabore um algoritmo que crie um tabuleiro de xadrez (8x8) colocando 0
nas casas brancas e 1 nas casas pretas.
'''

M = [0]*8
for i in range(8):
    M[i] = [0]*8
    for j in range(8):
        if (i + j) % 2 == 0:
            M[i][j] = 0
        else:
            M[i][j] = 1
        print(f'{M[i][j]}',end=' ')
    print()