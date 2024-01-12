'''
Dada uma lista de palavras, use a função map para criar uma nova lista
que contenha o comprimento de cada palavra.
'''

l = ['camarão', 'rebelde', 'fome', 'bicicleta', 'presente', 'Inglaterra']

l2 = list(map(lambda x: len(x), l))

print(l2)