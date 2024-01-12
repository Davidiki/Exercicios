'''
Elabore um programa que calcule N! (fatorial de N), sendo que o valor
inteiro de N é fornecido pelo usuário.
'''

num = int(input('Digite um número para descobrir seu fatorial: '))
cont = num

if num < 0:
    print('Fatorial é indefinido para números negativos')
else:
    fatorial = 1

while 1 < cont:
    fatorial *= cont
    cont -= 1

print(f'O fatorial de {num} é {fatorial}')

