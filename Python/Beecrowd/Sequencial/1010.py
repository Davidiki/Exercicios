cod1, uni1, preco1 = input().split()
cod2, uni2, preco2 = input().split()

print(f'VALOR A PAGAR: R$ {(int(uni1) * float(preco1)) + (int(uni2) * float(preco2)):.2f}')