'''Elabore um algoritmo que leia um numero inteiro
(max. 3 algarismos) e mostre os algarismos em separado.
Ex. NUM == 725 o algoritmo produzirá:
Centena = 7, Dezena = 2 e Unidade = 5.
'''

num = int(input('Digite um número (max. 3 algarismos): '))

centena = num // 100
dezena = num // 10 % 10
unidade = num % 10

print(f'Número: {num}\n'
      f'Centena: {centena}\n'
      f'Dezena: {dezena}\n'
      f'Unidade: {unidade}')
