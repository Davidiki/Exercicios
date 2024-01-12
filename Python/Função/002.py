'''
Escreva um programa em Python que implemente uma função potência, que
receba uma base e um expoente por parâmetro e retorne o valor da base
elevada ao expoente. O expoente é sempre maior ou igual a zero, e os
números são sempre inteiros. Peça uma base e um expoente, chame a função
e imprima o resultado.
'''
def potencia(base, expoente):
    if expoente >= 0:
        print(f'{base**expoente}')
    else:
        print(f'Expoente é menor que 0')

b = int(input('Digite a base: '))
e = int(input('Digite o expoente: '))

potencia(b,e)