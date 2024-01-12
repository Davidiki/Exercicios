'''
Elabore um algoritmo, que simule um Caixa de supermercado. Para isso,
leia preços e a quantidade comprada de cada produto. Calcule e
mostre o total que o cliente gastou em sua compra. Encerrar o algoritmo
quando for digitado 0 para o preço.
'''

soma = 0
while True:
    precoProduto = float(input('Digite o preço do produto comprado: '))
    if precoProduto == 0:
        break
    qtdComprada = int(input('Quantidade comprada: '))
    soma += (precoProduto * qtdComprada)
    

print(f'Total gasto: R$ {soma:.2f}')