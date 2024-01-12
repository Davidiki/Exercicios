'''
Faça um programa para ler 2 valores, calcular e escrever a soma dos
inteiros existentes entre os 2 valores lidos (incluindo os valores
lidos na soma). O programa deve validar que o 1º valor informado seja
menor que o 2º valor. O programa deve permitir que o usuário possa
executá-lo novamente.
'''

soma = 0
while True:
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o segundo valor: '))

    if valor2 < valor1:
        print('Valor inválido, o segundo valor deve ser maior do que o primeiro.')
    else:
        while valor1 <= valor2:
            soma += valor1
            valor1 += 1

        print(f"A soma dos inteiros entre os dois valores (incluindo-os) é: {soma}")

    resposta = input("Deseja executar o programa novamente? (Digite 's' para sim): ")
    if resposta != 's' or resposta != 'S':
        break




