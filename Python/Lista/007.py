'''
Elabore um algoritmo que leia um vetor com 20 elementos. A seguir,
troque o primeiro elemento com o décimo primeiro, o segundo com o
décimo segundo, etc., e mostre o vetor assim modificado.
'''

from random import randint
vetor = []

for i in range(20):
    vetor.append(randint(1, 50))

print(f'Vetor antes da alteração {vetor}')
vetor[0], vetor[10] = vetor[10], vetor[0]
vetor[1], vetor[11] = vetor[11], vetor[1]

print(f'Vetor depois da alteração {vetor}')