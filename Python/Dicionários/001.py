'''
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em uma lista. Depois, mostre quantas vezes cada valor foi
conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar números aleatórios, simulando os lançamentos dos dados.
'''

from random import randint

def geraLancamentos():
    return [randint(1,6) for i in range(100)]


def resultado(x):
    dado = {}
    for n in l:
        if n in dado:
            dado[n] += 1
        else:
            dado[n] = 1

    for n, q in sorted(dado.items()):
        print(f'{n}: {q}')


def exibeResultado(n):
    print('='* 50)

    for n in sorted(dado, key=dado.get):
        print('*' * 50)

    print(dado)



l = geraLancamentos()
print(l)

r = resultado(l)

print(exibeResultado(r))