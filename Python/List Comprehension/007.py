'''
Dada uma lista de strings, use a função map para criar uma nova lista
onde cada string é convertida para maiúsculas.
'''

lista = ['Amigo','Criança','Cavalo','Homen','Estudante']

lista2 = list(map(lambda x: str(x).upper(), lista))

print(lista)
print(lista2)
