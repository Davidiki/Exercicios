salario = float(input())
if salario <= 400:
    percentual = 15
    salarioReajustado = salario + (salario*0.15)
if salario > 400 and salario <= 800:
    percentual = 12
    salarioReajustado = salario + (salario*0.12)
if salario > 800 and salario <= 1200:
    percentual = 10
    salarioReajustado = salario + (salario*0.10)
if salario > 1200 and salario <= 2000:
    percentual = 7
    salarioReajustado = salario + (salario*0.07)
if salario > 2000:
    percentual = 4
    salarioReajustado = salario + (salario *0.04)

print(f'Novo salario: {salarioReajustado:.2f}\n'
      f'Reajuste ganho: {(salario * percentual)/100:.2f}\n'
      f'Em percentual: {percentual} %')