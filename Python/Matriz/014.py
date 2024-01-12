'''
Faça um programa em Python que gere as 5 notas (de 0 a 10) de 10 atletas
em uma competição. Armazene em uma matriz 10x5. Após, calcule a média
de cada atleta descartando a maior e menor nota obtida e diga qual
atleta venceu a competição, ou seja, o número da linha.
'''

from random import randint
notas = []

for i in range(10):
    notas.append([])
    for j in range(5):
        notas[i].append(randint(0,10))
    notas[i].sort()
    media = 0

    for j in range(1, 4):
        media += notas[i][j]
    media /= 3
    notas[i].append(media)

linha = 0

for i in range(1,10):
    if notas[i][5]> notas[linha][5]:
        linha = i

for i in range(10):
    for j in range(5):
        print(f'{notas[i][j]}',end='  ')
    if i == linha:
        print(f' -> Média = {notas[i][5]:.2f} -> Campeão!!')
    else:
        print(f' -> Média = {notas[i][5]:.2f}')
