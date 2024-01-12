'''
Elabore um programa que leia uma matriz 5x5 e verifique se esta matriz
é simétrica. Uma matriz para ser simétrica deve ter A[i][j] == A[j][i]

'''

M = [0] * 5
for i in range(5):
    M[i] = [0] * 5
    for j in range(5):
        M[i][j] = (i + 1) + j
        print(f'{M[i][j]:02}', end=' ')
    print()

simetrico = True
for i in range(5):
    for j in range(5):
        if M[i][j] != M[j][i]:
            simetrico = False
            break

print()
if simetrico:
    print("A matriz é simétrica.")
else:
    print("A matriz não é simétrica.")

