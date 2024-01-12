'''Faça um programa que leia um número e, caso ele seja
positivo, calcule e mostre:
• O número digitado ao quadrado
• A raiz quadrada do número digitado'''

num = int(input('Digite um número: '))
raizQuadrada = int(num ** 0.5)

print(f'A raiz quadrada de {num} é {raizQuadrada}')