'''
Dada uma lista de palavras, use a função filter para criar uma nova
lista contendo apenas as palavras que têm mais de 5 letras.
'''

l = ['Criança', 'Carro', 'David', 'Bicicleta', 'Casa', 'Cama', 'Caminhão', 'Russia', 'Julia', 'Python', 'Dança', 'Samba']

def maior5Letras(x):
    return len(x) > 5


l2 = list(filter(maior5Letras, l))

print(l2)