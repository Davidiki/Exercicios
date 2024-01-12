'''
Construa um programa que verifique se um número fornecido pelo usuário
é primo ou não.
'''

num = int(input('Digite um número inteiro: '))

if num > 1:
    div = 2
    ehprimo = True

    while div <= num // 2:
        if num % div == 0:
            ehprimo = False
            break
        div += 1
    if ehprimo:
        print(f'{num} é um número primo.')
    else:
        print(f'{num} não é um número primo.')
else:
    print('O número deve ser maior que 1 para ser considerado primo.')