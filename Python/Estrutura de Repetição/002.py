'''
Elabore um algoritmo para mostrar a tabuada de um número N qualquer
lido pelo teclado. Por exemplo, se N == 7,
deverá ser mostrado: 7*1, 7*2, 7*3, ... 7*10.
'''

num = int(input('Digite o número da tabuada que deseja: '))
cont = 1

while cont <= 10:
    mult = num * cont
    print(f'{num}x{cont} = {mult}')
    cont += 1