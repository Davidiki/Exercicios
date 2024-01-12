'''
Escreva um programa para ler 10 números do usuário e calcular a
soma dos números pares e a soma dos números ímpares.
'''

cont = 1
somaPares = 0
somaImpares = 0

while cont <= 10:
    num = int(input(f'Digite o {cont}º número: '))

    if num % 2 == 0:
        somaPares += num
    else:
        somaImpares += num
    cont += 1

print(f'Soma dos números pares: {somaPares}\n'
      f'Soma dos números ímpares: {somaImpares}')