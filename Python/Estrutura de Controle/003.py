'''3.) Elabore um algoritmo que leia a velocidade máxima
permitida em uma rodovia e também a velocidade que um determinado
veículo trafega. Verificar se ele sofrerá multa (caso em que sua
velocidade seja superior a permitida) ou não.
'''

velocidadeMaxima = int(input('Velocidade máxima permitida: '))
velocidaVeiculo = int(input('Velocidade do veículo: '))

if velocidaVeiculo >= velocidadeMaxima:
    print('Motorista será multado')
else:
    print('Motorista não será multado')