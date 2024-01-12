'''
Defina a função media_digitos que recebe como argumento um número
natural e devolve a média dos seus dígitos
'''

def media_digitos(n):
    return sum(list(map(int, str(n)))) / len(str(n))
num = int(input('Informe um número -> '))
print(f'Média dos números -> {media_digitos(num)}')