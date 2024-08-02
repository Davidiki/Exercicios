codigo, quantidade = map(int, input().split())

if codigo == 1:
    preco = 4.00
if codigo == 2:
    preco = 4.50
if codigo == 3:
    preco = 5.00
if codigo == 4:
    preco = 2.00
if codigo == 5:
    preco = 1.50

print(f'Total: R$ {quantidade*preco:.2f}')