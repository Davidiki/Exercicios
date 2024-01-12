'''
Escreva um programa em Python que contenha uma função que peça um
número e verifique se ele é par ou ímpar. No principal, chame a função.
'''

def parImpar(x):
    if num % 2 == 0:
        print(f'{num} é par')
    else:
        print(f'{num} é impar')


num = int(input('Digite um número: '))
parImpar(num)