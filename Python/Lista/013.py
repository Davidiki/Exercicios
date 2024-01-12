'''
Idem ao anterior para o algoritmo  Select Sort.

'''

from random import randint
lista = []
for i in range(10):
    lista.append(randint(1, 50))

print(lista)

for i in range(len(lista)):
    min_index = i
    for j in range(i + 1, len(lista)):
        if lista[j] < lista[min_index]:
            min_index = j
    lista[i], lista[min_index] = lista[min_index], lista[i]

print(lista)