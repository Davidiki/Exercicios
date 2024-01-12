'''
Elabore um programa em Python que gere uma matriz 5x5 e calcule e mostre
a diagonal principal e a secundária.
'''

matriz = [0]*5
for i in range(5):
    matriz[i] = [0]*5
    for j in range(5):
        matriz[i][j] = (i*5) + j
        print(f'{matriz[i][j]:02}',end=' ')
    print()


print("\nDiagonal Principal")
for i in range(5):
    print(f"{matriz[i][i]:02}",end=" ")


print("\n\nDiagonal Principal")
for i in range(5):
    for j in range(5):
        if i == j:
            print(f"[{matriz[i][j]:02}]",end=" ")
        else:
            print(f"[ ]", end=" ")
    print()


print("\nDiagonal Secundária")
for i in range(5):
    print(f"{matriz[i][4-i]:02}",end=" ")

print("\n\nDiagonal Secundária")
for i in range(5):
    for j in range(5):
        if i + j == 4:
            print(f"[{matriz[i][j]:02}]",end=" ")
        else:
            print(f"[ ]", end=" ")
    print()