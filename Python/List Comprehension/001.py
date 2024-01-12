'''
Defina a função soma_nat que recebe como argumento um número natural n
e devolve a soma de todos os números naturais até n.
'''

def soma_nat(n):
    return sum([i for i in range(1, n+1)])

num = int(input('Digite um número: '))
print(f'A soma de todos os números de 1 à {num} é {soma_nat(num)}')