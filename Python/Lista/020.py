'''
Faça um programa em Python para gerar uma lista de 20 números aleatórios
entre 1 e 50. Imprima a lista. Após isto, deverá ser lido um número
qualquer e verificar se esse número existe na lista ou não. Se existir,
gerar uma nova lista sem esse número (remova todas as ocorrências do
número). Imprima a nova lista.
'''

from random import randint
l = []
for i in range(20):
    l.append(randint(1,50))
print(l)

num = int(input('Número: '))

if num in l:
    l.remove(num)
    print(f'{num} removido da lista\n'
          f'Nova lista: {l} ')
else:
    print(f'{num} não existe na lista')