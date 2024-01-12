'''
Faça um programa em Python que gere um triângulo de altura e lados n e
base 2*n-1. Por exemplo, a saída para n = 6 seria:
                     *
                    ***
                   *****
                  *******
                 *********
                ***********
'''

n = int(input('Digite um valor inteiro: '))

for i in range(1, n + 1):
    print(' ' * (n - i), end='')
    print('*' * (2 * i - 1))
