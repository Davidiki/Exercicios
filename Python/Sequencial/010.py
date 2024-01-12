'''Implemente um programa para ler o preço do litro do
combustível de um carro, ler o desempenho do veículo (km/l) e a
distância entre duas cidades (km), e informar quantos litros, e
quanto dinheiro vai ser gasto para fazer uma viagem entre as
duas cidades.'''

precoCombustivel = float(input(f'Preço do litro do combustível: '))
kmPorLitro = float(input('Quilometros por Litro: '))
distanciaCidades = int(input('Distância entre cidades em KM: '))
litrosGastos = distanciaCidades / kmPorLitro
dinheiroGasto = litrosGastos * precoCombustivel

print(f'Litros gastos na viagem: {litrosGastos:.1f} litros\n'
f'Dinheiro gasto na viagem: R$ {dinheiroGasto:.2f}')