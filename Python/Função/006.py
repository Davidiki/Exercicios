'''
Faça um programa em Python que gere uma matriz 10 x 10 de inteiros e
crie funções para calcular e retornar o maior elemento de uma
determinada coluna (informada por parâmetro) e o menor elemento de uma
determinada linha (informada por parâmetro). Peça a coluna e a linha,
chame os respectivos métodos e mostre o resultado.
'''


from random import randint

def geraMatriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(randint(1, 100))
        matriz.append(linha)
    return matriz

def imprimeMatriz(matriz):
    for linha in matriz:
        for elemento in linha:
            print(f'{elemento:03}', end=' ')
        print()

def menorValorLinha(matriz, linha):
    menor = matriz[linha][0]
    for elemento in matriz[linha]:
        if elemento < menor:
            menor = elemento
    return menor

def maiorValorColuna(matriz, coluna):
    maior = matriz[0][coluna]
    for linha in matriz:
        if linha[coluna] > maior:
            maior = linha[coluna]
    return maior

linhas = int(input('Digite a quantidade de linhas: '))
colunas = int(input('Digite a quantidade de colunas: '))

matrizGerada = geraMatriz(linhas, colunas)
print('Matriz gerada:')
imprimeMatriz(matrizGerada)

linhaEscolhida = int(input('Digite a linha que deseja encontrar o menor valor: '))
colunaEscolhida = int(input('Digite a coluna desejada para encontrar o maior valor: '))

menorValor = menorValorLinha(matrizGerada, linhaEscolhida)
print(f'O menor valor na linha {linhaEscolhida} é: {menorValor}')

maiorValor = maiorValorColuna(matrizGerada, colunaEscolhida)
print(f'O maior valor na coluna {colunaEscolhida} é: {maiorValor}')
