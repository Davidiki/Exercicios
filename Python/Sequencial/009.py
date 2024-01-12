'''Implemente um programa para ler o salário mensal atual de
um funcionário e o percentual de reajuste. Calcular e escrever o
valor do novo salário.'''

salarioInicial = float(input(f'Digite o valor do salário antes do reajuste: '))
reajuste = int(input('Porcentagem de reajuste: '))
salarioFinal = salarioInicial + (salarioInicial * (reajuste / 100))

print(f'Salário Inicial: R$ {salarioInicial:.2f}\n'
      f'Reajuste: {reajuste}%\n'
      f'Salário Após reajuste: R$ {salarioFinal:.2f}')