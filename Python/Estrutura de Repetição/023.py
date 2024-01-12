'''
Faça um programa que leia um número positivo e imprima seus divisores.
'''

num = int(input('Digite um número: '))

for i in range(1, num):
    if num % i == 0:
        print(i, end=' ')

