'''Escreva um programa que pergunte a quantidade de km
percorridos por um carro alugado pelo usuário, assim como a
quantidade de dias pelos quais o carro foi alugado. Calcule o
preço a pagar, sabendo que o carro custa R$ 60 por dia e
R$ 0,15 por km rodado.'''

kmPercorrido = int(input('Quilometros percorridos: '))
diasAlugado = int(input('Quantidade de dias de aluguel: '))


print(f'KM percorrido: {kmPercorrido}\n'
      f'Dias de aluguel: {diasAlugado}\n'
      f'Valor a pagar: R$ {(diasAlugado * 60) + (kmPercorrido * 0.15):.2f}')