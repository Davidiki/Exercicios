'''
Leia a distância em Km e a quantidade de litros de gasolina
consumidos por um carro em um percurso, calcule o consumo em
Km/l e escreva uma mensagem de acordo com a tabela abaixo:

Consumo         Km/l               Mensagem
Menor que        8              Venda o carro
Entre         8 e 14               Econômico
Maior que       14              Super econômico
'''


distanciaPercorrida = int(input('Distância percorrida: '))
kmL = int(input('Quilometros por litro: '))
consumo = distanciaPercorrida / kmL

if consumo < 8:
    print('Venda o carro')
elif consumo >= 8 and consumo <= 14:
    print('Ecônomico')
elif consumo > 14:
    print('Super econômico')