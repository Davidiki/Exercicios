'''1.) Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas. Faça um programa que receba o salário fixo de um funcionário e o valor de suas vendas, calcule e mostre a comissão e o salário final do funcionário. '''

salarioFixo = float(input('Digite o valor do salário fixo de um funcionário: '))
vendas = float(input('Digite o valor de vendas: '))
comissao = vendas * 0.04
salarioFinal = salarioFixo + comissao
print(f'Salário Fixo do vendedor: R$ {salarioFixo:.02f}\n'
      f'Valor total de vendas: R$ {vendas:.02f}\n'
      f'Comissão: R$ {comissao:.02f}\n'
      f'Salário Final: R$ {salarioFinal:.02f}')
