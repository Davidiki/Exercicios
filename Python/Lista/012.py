'''
Elabore um algoritmo que leia um vetor de 10 elementos e ordene os
vetores de forma crescente. (Pesquise o algoritmo Bubble Sort)
'''

from random import randint
lista = []
for i in range(10):
    lista.append(randint(1, 50))

print(lista)
for i in range(10):
    for j in range(10):
        if lista[i] < lista[j]:
            lista[i], lista[j] = lista[j], lista[i]

print(lista)