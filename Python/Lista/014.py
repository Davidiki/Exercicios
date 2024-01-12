'''
Elabore um algoritmo que leia dois vetores A e B de 10 elementos cada
(já ordenados de forma crescente) e calcule o vetor C, formado pela
intercalação dos vetores lidos (A e B).
'''

from random import randint
a = []
b = []
c = []

for i in range(10):
    a.append(randint(1, 50))
    b.append(randint(1, 50))
a = sorted(a)
b = sorted(b)

for j in range(10):
    c.append(a[j])
    c.append(b[j])

print(f'{a}\n'
      f'{b}\n'
      f'{c}')