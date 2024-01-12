'''
Elabore um algoritmo, usando a estrutura PARA, que leia um número
inteiro e mostre todos os seus divisores. Ex. se n == 20,
deverá ser mostrado: 1  2  4  5  10 e 20.
'''


num = int(input('Digite um número inteiro e descubra seus divisores: '))

for i in range(1, num):
    if num % i == 0:
        print(i,end=' ')