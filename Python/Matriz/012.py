'''
Faça um programa em Python que gere uma matriz 5x5 com valores entre
1 e 50. Imprima a matriz e troque uma linha por outra linha informada
pelo usuário. Mostre a matriz após a troca.
'''

from random import randint

matriz = [0]*5

print('Matriz antes da troca')
for i in range(5):
    matriz[i] = [0]*5
    for j in range(5):
        matriz[i][j] = randint(1,50)
        print(f'{matriz[i][j]:02}',end=' ')
    print()

linha1 = int(input('\nDigite a primeira linha que deseja trocar [Escolha entre 0 e 4]: '))
linha2 = int(input('Digite a segunda linha que deseja trocar [Escolha entre 0 e 4]: '))
print()
for i in range(5):
    matriz[linha1][i], matriz[linha2][i] = matriz[linha2][i], matriz[linha1][i]
    for j in range(5):
        print(f'{matriz[i][j]:02}',end=' ')
    print()