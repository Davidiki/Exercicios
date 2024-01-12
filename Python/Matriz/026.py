'''
Elabore um programa que leia uma matriz 4x12. Cada coluna indica um mês
do ano e cada linha uma semana do respectivo mês. Os valores
armazenados representam o total de peças produzidas por uma
determinada fábrica.

Calcule:
A) Total de peças produzidas em cada mês;
B) Total de peças produzidas no ano;
C) Qual foi a semana e qual o mês onde houve a maior produção.
'''

from random import randint

M = [0] * 4
totalAno = 0
maiorSemana = 0
maiorMes = 0

for i in range(4):
    M[i] = [0] * 12
    for j in range(12):
        M[i][j] = randint(30, 99)
        print(f'{M[i][j]:02}', end=' ')
        totalAno += M[i][j]
    print()

totalMes = [0] * 12
for j in range(12):
    for i in range(4):
        totalMes[j] += M[i][j]

for i in range(4):
    for j in range(12):
        if M[i][j] > M[maiorSemana][maiorMes]:
            maiorSemana = i
            maiorMes = j

print("\nTotal de peças produzidas em cada mês:")
for j in range(12):
    print(f'Mês {j + 1}: {totalMes[j]} peças')

print(f'\nTotal de peças produzidas no ano: {totalAno} peças')
print(f'\nMaior produção na semana {maiorSemana + 1} do mês {maiorMes + 1} com {M[maiorSemana][maiorMes]} peças.')
