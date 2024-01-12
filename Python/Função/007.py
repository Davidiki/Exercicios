'''
Faça um programa que leia uma data e determine se ela é válida, ou
seja, verifique se o mês está entre 1 e 12, e se o dia existe naquele
mês. Note que Fevereiro tem 29 dias em anos bissextos, e 28 dias em
anos não bissextos. Faça funções para validação e para verificar se o
ano é bissexto.
'''

def diaValido(dia, mes, ano):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 1 <= dia <= 31
    elif mes in [4, 6, 9, 11]:
        return 1 <= dia <= 30
    elif mes == 2:
        if anoBissexto(ano):
            return 1 <= dia <= 29
        else:
            return 1 <= dia <= 28
    else:
        return False

def anoBissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

# Solicita a data ao usuário
dia = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))

# Verifica se a data é válida
if 1 <= mes <= 12 and diaValido(dia, mes, ano):
    print('A data é válida.')
else:
    print('A data é inválida.')
