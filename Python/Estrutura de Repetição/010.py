'''
Igual ao exercício anterior, mas pedir antes do laço a quantidade de
números a serem lidos.
'''

qtdNumeros = int(input('Quantidade de números a serem lidos: '))
cont = 1
somaPares = 0
somaImpares = 0

while cont <= qtdNumeros:
    num = int(input(f'Digite o {cont}º número: '))

    if num % 2 == 0:
        somaPares += num
    else:
        somaImpares += num

    cont += 1

print(f'Soma dos números pares: {somaPares}\n'
      f'Soma dos números ímpares: {somaImpares}')