'''
Dada uma lista de strings, use a função filter para criar uma nova lista
contendo apenas as strings que não estão vazias.
'''

def listaNaoVazia(s):
    return len(s) > 0

listaStrings = ['', 'Python', '', 'Programação', 'Lista', '', 'Não', 'Vazia']

l = list(filter(listaNaoVazia, listaStrings))

print(l)
