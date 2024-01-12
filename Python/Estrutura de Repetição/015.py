'''
O número 3025 tem a seguinte característica:
30 + 25 = 55
552 = 3025
Elabore um programa para mostrar todos os números de 4 algarismos que
possuem esta mesma característica.
'''

num = 1000

while num < 10000:
    parte1 = num // 100
    parte2 = num % 100

    somaPartes = parte1 + parte2
    quadradoSoma = somaPartes ** 2

    if quadradoSoma == num:
        print(f'{parte1} + {parte2} = {somaPartes}\n'
              f'{somaPartes}² = {quadradoSoma}\n')

    num += 1