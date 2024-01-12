'''
Elabore um algoritmo que leia um vetor capaz de armazenar 20 valores
inteiros e, em seguida, gere outros dois vetores, um formado pelos
valores pares e o outro pelos valores ímpares
'''

from random import randint

vetor1 = []
vetor2 = []
vetor3 = []

for i in range(20):
    vetor1.append(randint(1, 100))
    if vetor1[i] % 2 == 0:
        vetor2.append(vetor1[i])
    else:
        vetor3.append(vetor1[i])

print(f'{vetor1}\n'
      f'{vetor2}\n'
      f'{vetor3}')