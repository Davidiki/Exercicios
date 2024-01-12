'''
Escreva um programa em Python que contenha uma função que retorne True
caso o argumento passado seja primo e False caso contrário. O argumento
será sempre um valor inteiro. Peça um número, chame o método e imprima
se o mesmo é número primo ou não.
'''

def ehPrimo(n):
    if num < 2:
        return false
    for i in range(2,num):
        if num % i == 0:
            return False
        return True

num = int(input('Digite um número: '))
if ehPrimo(num):
    print(f'{num} é primo')
else:
    print(f'{num} não é primo')