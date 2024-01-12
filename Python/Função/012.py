'''
Faça um programa que leia um número inteiro positivo impar N e calcule
o fatorial duplo desse número. O fatorial duplo é definido como o
produto de todos os números naturais ímpares de 1 até algum número
natural ímpar N. Assim, o fatorial duplo de 5 é: 5!! = 1 * 3 * 5 = 15
Faça funções para validação da entrada e para o cálculo do fatorial
duplo.
'''


def fatorialDuplo(N):
    fat = 1
    for i in range(N, 1, -1):
        if i % 2 != 0:
            fat *= i
    return fat

num = int(input('Digite um número para descobrir seu fatorial duplo: '))
print(f'O fatorial duplo de {num} é {fatorialDuplo(num)}')