'''
Faça um programa em Python que gere 10 elementos aleatórios
(entre 1 e 50) armazenando em uma lista e uma opção. Se a opção for 1,
mostrar o vetor na ordem direta, se a opção for 2, mostrar o vetor na
ordem inversa.
'''

from random import randint

lista = []

for i in range(10):
    lista.append(randint(1, 50))

num = int(input('Digite 1 para mostrar o vetor na ordem direta, ou digite 2 para mostrar o vetor na orddem indireta: '))

if num == 1:
    print(lista)
if num == 2:
    print(lista[::-1])
else:
    print('Opção inválida!')