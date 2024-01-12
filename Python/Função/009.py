'''
Faça um programa que receba a data atual e exiba-a na tela no formato
textual por extenso. Exemplo: Data: 01/01/2021, Imprimir: 1 de janeiro
de 2021. Faça funções para retornar a data por extenso e utilize as
funções do exercício anterior para validar a entrada da data.
'''


def diaValido(dia, mes, ano):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 1 <= dia <= 31
    if mes in [4, 6, 9, 11]:
        return 1 <= dia <= 30
    if mes == 2:
        if anoBissexto(ano):
            return 1 <= dia <= 29
        else:
            return 1 <= dia <= 28
    else:
        return False


def anoBissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)


def imprimeData(dia, mes, ano):
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
             'Novembro', 'Dezembro']
    if diaValido(dia, mes, ano):
        data_extenso = f'{dia} de {meses[mes - 1]} de {ano}'
        return data_extenso
    else:
        return 'Data Inválida'

data = input('Digite a data atual (no formato DD/MM/AAAA): ').split('/')
data = [int(valor) for valor in data]

print(imprimeData(data[0], data[1], data[2]))
