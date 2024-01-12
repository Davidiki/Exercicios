'''
Elabore um algoritmo que leia um número inteiro e determine quantos
algarismos ele possui. Exemplos:

Num == 23456  5 algarismos
Num == 9876789  7 algarismos

'''

num = int(input("Digite um número: "))

cont = 0

if num == 0:
    cont = 1
else:
    while num != 0:
        num //= 10
        cont += 1

print(f"O número tem {cont} algarismos.")
