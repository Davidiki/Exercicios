'''
Elabore um algoritmo que leia 2 vetores de 10 números inteiros cada e
em seguida calcule e imprima um terceiro vetor formado pela soma dos
valores respectivos dos vetores lidos.
'''

from random import randint
vetor1 = []
vetor2 = []
vetor3 = []

for i in range(10):
    vetor1.append(randint(1, 100))
    vetor2.append(randint(1, 100))
    vetor3.append(vetor1[i] + vetor2[i])

print(f'Vetor 1 {vetor1}\n'
      f'Vetor 2 {vetor2}\n'
      f'Vetor 3 {vetor3}')