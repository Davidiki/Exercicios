valor = float(input())

valor_em_centavos = int(valor * 100)

nota100 = valor_em_centavos // 10000
valor_em_centavos %= 10000

nota50 = valor_em_centavos // 5000
valor_em_centavos %= 5000

nota20 = valor_em_centavos // 2000
valor_em_centavos %= 2000

nota10 = valor_em_centavos // 1000
valor_em_centavos %= 1000

nota5 = valor_em_centavos // 500
valor_em_centavos %= 500

nota2 = valor_em_centavos // 200
valor_em_centavos %= 200

moeda1r = valor_em_centavos // 100
valor_em_centavos %= 100

moeda50 = valor_em_centavos // 50
valor_em_centavos %= 50

moeda25 = valor_em_centavos // 25
valor_em_centavos %= 25

moeda10 = valor_em_centavos // 10
valor_em_centavos %= 10

moeda5 = valor_em_centavos // 5
valor_em_centavos %= 5

moeda1_centavo = valor_em_centavos

print(f'NOTAS:\n'
      f'{nota100} nota(s) de R$ 100.00\n'
      f'{nota50} nota(s) de R$ 50.00\n'
      f'{nota20} nota(s) de R$ 20.00\n'
      f'{nota10} nota(s) de R$ 10.00\n'
      f'{nota5} nota(s) de R$ 5.00\n'
      f'{nota2} nota(s) de R$ 2.00\n'
      f'MOEDAS:\n'
      f'{moeda1r} moeda(s) de R$ 1.00\n'
      f'{moeda50} moeda(s) de R$ 0.50\n'
      f'{moeda25} moeda(s) de R$ 0.25\n'
      f'{moeda10} moeda(s) de R$ 0.10\n'
      f'{moeda5} moeda(s) de R$ 0.05\n'
      f'{moeda1_centavo} moeda(s) de R$ 0.01')
