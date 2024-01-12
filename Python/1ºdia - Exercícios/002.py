'''
Escreva um programa que gere um triângulo lateral de altura 2*n-1 e n
largura. Por exemplo, a saída para n = 4 seria:
*
**
***
****
***
**
*
'''

n = int(input('Digite um valor inteiro: '))

for i in range(1, n + 1):
    print('*' * i)

for i in range(n - 1, 0, -1):
    print('*' * i)
