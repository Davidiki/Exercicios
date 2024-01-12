'''
Faça um programa em Python que gere 10 elementos aleatórios
(entre 1 e 50) armazenando na lista A e um valor x. Criar o vetor B
contendo os elementos do vetor A multiplicados por x. Imprima os dois
vetores.
'''
from random import randint
a = []
b = []
x = int(input('Digite um número para ser multiplicado: '))

for i in range(10):
    a.append(randint(1, 50))
    b.append(a[i] * x)

print(f'{a}\n'
      f'{b}')