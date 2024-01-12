'''
Elabore um programa para mostrar a sequência dos N primeiro números da
série de Fibonacci:
1 1 2 3 5 8 13 21 34 55 89 ....
Sempre o próximo elemento é a soma dos dois anteriores, assim, no
exemplo o próximo é 144.
'''

num = int(input("Digite o número de termos da série de Fibonacci que deseja gerar: "))

a = 1
b = 1
cont = 1

while cont <= num:
    print(a, end=" ")
    a, b = b, a + b
    cont += 1
