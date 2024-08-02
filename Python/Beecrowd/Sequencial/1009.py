nomeVendedor = input()
salarioFixo = float(input())
totalVendas = float(input())
comissao = totalVendas * 0.15
print(f'TOTAL = R$ {salarioFixo + comissao:.2f}')