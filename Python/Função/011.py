'''
Faça uma função que receba um número N e retorne a soma dos algarismos
de N!. Ex: se N = 4, N! = 24. Logo, a soma de seus algarismos
e 2 + 4 = 6. Faça função para o cálculo do fatorial e para a soma
dos dígitos.
'''

def fatorial(N):
    fat = 1
    for i in range(1, N + 1):
        fat *= i
    return fat

def somaDigitos(numero):
    soma = 0
    for digito in str(numero):
        soma += int(digito)
    return soma

# Exemplo de uso
N = int(input('Digite um número N: '))
fatN = fatorial(N)
somaDig = somaDigitos(fatN)

print(f'A soma dos algarismos de {N}! é: {somaDig}')
