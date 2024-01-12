'''
Idem ao anterior, porem gerando o vetor união de A com B (Todos os elementos de A e somente os elementos de B que não existem em A).
'''

from random import randint

a = []
b = []
c = []

for i in range(10):
    a.append(randint(1,50))
    b.append(randint(1,50))

for j in range(10):
    if a[j] not in b:
        c.append(a[j])
    if b[j] not in a and b[j]not in c:
        c.append(b[j])
print(f'{a}\n'
      f'{b}\n'
      f'{c}')