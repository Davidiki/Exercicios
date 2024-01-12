'''Escreva um programa para ler um uma temperatura em graus
Fahrenheit, calcular e escrever o valor correspondente em
graus Celsius:
C = ((F – 32)/9)*5'''

f = int(input('Temperatura em Celsius: '))
c = ((f - 32) / 9) * 5

print(f'Temperatura em Fahrenheit: {f}º\n'
      f'Temperatura em Celsius: {c:.1f}º')