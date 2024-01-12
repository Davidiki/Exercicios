'''
Elabore um programa em Python que declare uma matriz quadrada de 10
linhas por 10 colunas e verifique se a matriz é simétrica em relação à
diagonal principal. A matriz simétrica é aquela em que todos os
elementos A( i , j) = A( j , i) para quaisquer valores de i e j. Assim,
A[2,1] deverá ser igual a A[1,2], e A[3,5] deverá ser igual a A[5,3] e
assim por diante. Imprimir mensagem “Matriz Simétrica” ou “Matriz não
Simétrica”.
'''


matriz = [0] * 10
for i in range(10):
    matriz[i] = [0] * 10
    for j in range(10):
        matriz[i][j] = int(input(f"{i}{j} -> "))

print("\nMatriz informada")
for i in range(10):
    for j in range(10):
        print(f"{matriz[i][j]:02}", end=' ')
    print()

sim = True
for i in range(10):
    for j in range(i + 1, 10):
        if matriz[i][j] != M[j][i]:
            sim = False

if sim:
    print("\nMatriz simétrica em relação à diagonal principal")
else:
    print("\nMatriz não é simétrica em relação à diagonal principal")
