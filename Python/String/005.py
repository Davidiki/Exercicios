'''
Fazer um programa em Python para verificar se uma determinada String é
palíndromo. Exs.: ANA - MUSSUM – OVO
'''

palavra = input('Digite uma palavra e verifique se é um palíndromo : ')
if palavra == palavra[::-1]:
    print(f'{palavra} é um palíndromo')
else:
    print(f'{palavra} não é um palíndromo')