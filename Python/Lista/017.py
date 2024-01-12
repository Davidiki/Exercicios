'''
Faça um programa que gere uma lista de 20 números aleatórios
entre 1 e 10. Leia um número x entre 1 e 10. Imprima a lista e mostre
quantos números iguais a x tem na lista.
'''
from random import randint

lista = []

for i in range(20):
    lista.append(randint(1,10))


x = int(input('Digite um número entre 1 e 10: '))
print(f'Existem {lista.count(x)} números iguais à {x} na lista')