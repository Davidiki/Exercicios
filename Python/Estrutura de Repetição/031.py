'''
Elabore um algoritmo, usando a estrutura PARA, que leia um número
inteiro e calcule o seu fatorial. Ex. o fatorial de n==5 é 120,
pois: 5! = 5*4*3*2*1== 120.

'''

num = int(input('Digite um número inteiro para descobrir seu fatorial: '))
fatorial = 1
for i in range(num, 1, -1):
    fatorial *= i

print(f'O fatorial de {num} é {fatorial}')