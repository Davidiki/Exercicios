'''
Faça um programa que calcule e mostre a soma dos 50 primeiros números
pares.
'''

soma = 0
cont = 1
par = 0
while par < 50:
    if cont % 2 == 0:
        print(cont, end=' ')
        soma += cont
        par += 1
    cont += 1

print(f'\nSoma dos 50 primeiros números pares. {soma}')