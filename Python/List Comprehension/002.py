'''
Defina a função quadrados que recebe como argumento um número natural n
devolve a lista dos n primeiros quadrados perfeitos.
'''

def quadrados(n):
    return [i ** 2 for i in range(n + 1)]

num = int(input('Digite um número: '))

print(f'O quadrados perfeitos de 1 à {num} são: {quadrados(num)}')