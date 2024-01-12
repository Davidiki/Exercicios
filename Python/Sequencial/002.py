'''2. ) Elabore um algoritmo que leia um valor em reais
(R$) e mostre sua conversão para dólares ($).
Para isto o algoritmo deverá solicitar ao usuário a cotação
do dólar. Mostre o resultado.
'''

valorReais = float(input(f'Valor em Reais(R$): '))
cotacaoDolar = float(input(f'Cotação atual do dólar(US$): '))
valorDolar = float(valorReais / cotacaoDolar)
print(f'\n\nValor em Reais: {valorReais:.2f}\n'
      f'Valor convertido em dólar: {valorDolar:.2f}')