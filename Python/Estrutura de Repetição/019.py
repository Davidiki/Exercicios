'''
Faça um programa que mostre os cinco primeiros múltiplos de 3,
considerando números maiores que 0.
'''


cont = 0
num = 1

while cont < 5:
    if num % 3 == 0:
        print(num, end=' ')
        cont += 1
    num += 1
