'''
Elabore um algoritmo que leia dois (A e B) vetores de 10 elementos inteiros cada. Calcule um terceiro vetor formado pela intersecção ( C ) dos vetores lidos.
(Elementos que existem em ambos os vetores A e B, não importando suas posições).
'''

from random import randint
a = []
b = []
c = []
for i in range(10):
    a.append(randint(1,50))
    b.append(randint(1,50))

for j in range(10):
    if a[j] in b:
        c.append(a[j])

print(f'{a}\n'
      f'{b}\n'
      f'{c}')