'''
Elabore um algoritmo que leia idades de um grupo de pessoas e, calcule
e mostre a média das idades lidas. O algoritmo deverá ser encerrado
quando a idade lida for zero (0).
'''

soma = 0
cont = 0

while True:
    idade = int(input('Digite a idade: '))

    if idade == 0:
        break
    soma += idade
    cont += 1

if cont == 0:
    print("Nenhuma idade foi inserida.")
else:
    media = soma / cont
    print(f'Média de idade: {media}')
