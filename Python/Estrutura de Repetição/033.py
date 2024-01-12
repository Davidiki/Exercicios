'''
Elabore um algoritmo, usando a estrutura PARA, que leia um número e
verifique se ele é primo. Um número para ser primo tem no máximo
dois divisores: 1 e ele próprio.

'''

num = int(input('Digite um número e veja se ele é primo: '))
ehprimo = 0
for i in range(1, num):
    if num % i == 0:
        ehprimo += 1

if ehprimo >= 2:
    print(f'{num} não é um número primo')
else:
    print(f'{num} é um número primo')