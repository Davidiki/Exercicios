'''
Gere uma lista 20 números aleatórios entre 1 e 50 e mostre qual o maior
valor da lista, o menor e a média dos valores.
'''
from random import randint

lista = []

for i in range(20):
    lista.append(randint(1,50))

maior = max(lista)
menor = min(lista)
media = sum(lista) / len(lista)

print(f'{lista}\n'
      f'Maior: {maior}\n'
      f'Menor: {menor}\n'
      f'Média: {media}')