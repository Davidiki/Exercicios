'''
Faça um programa em Python que imprima todos os números primos de um
intervalo informado pelo usuário. Utilize o método do exercício 4 para
verificar se o número é primo ou não.
'''
def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def imprimir_primos_intervalo(inicio, fim):
    primos = []
    for num in range(inicio, fim + 1):
        if eh_primo(num):
            primos.append(num)
    return primos

inicio = int(input('Digite o início do intervalo: '))
fim = int(input('Digite o fim do intervalo: '))

resultado = imprimir_primos_intervalo(inicio, fim)
print(f'Números primos no intervalo de {inicio} a {fim}: {resultado}')
