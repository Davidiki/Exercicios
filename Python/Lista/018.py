'''
Faça um programa que gere aleatoriamente duas listas de 10 posições
(valores entre 1 e 50) e calcule outra lista contendo, nas posições
pares os valores da primeira lista e nas posições ímpares os valores da
segunda lista.
'''

from random import randint

lista1 = []
lista2 = []
lista3 = []

for i in range(10):
    lista1.append(randint(1,50))
    lista2.append(randint(1,50))

for i in range(10):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

print(f'{lista1}\n'
      f'{lista2}\n'
      f'{lista3}')