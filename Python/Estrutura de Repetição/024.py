'''
Escreva um programa que leia um número inteiro e calcule a soma de
todos os divisores desse número, com exceção dele próprio.
Ex: a soma dos divisores do
número 66 é 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78
'''


num = int(input('Digite um número: '))
soma = 0

for i in range(1, num):
    if num % i == 0:
        print(i, end=' ')
        soma += i

print(f'\nSoma = {soma}')