'''
Faça um programa para entrar com a data de nascimento, data atual e
mostrar a idade da pessoa. Utilize as funções do exercício anterior
para validar a entrada das datas.
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

def idade(dataNascimento, dataAtual):
    diaNascimento, mesNascimento, anoNascimento = dataNascimento
    diaAtual, mesAtual, anoAtual = dataAtual

    if (anoNascimento, mesNascimento, diaNascimento) <= (anoAtual, mesAtual, diaAtual):
        anos = anoAtual - anoNascimento
        meses = mesAtual - mesNascimento
        dias = diaAtual - diaNascimento

        if dias < 0:
            meses -= 1
            dias += 30  # Considerando um mês de 30 dias para simplificar

        if meses < 0:
            anos -= 1
            meses += 12

        return anos, meses, dias
    else:
        return None

dataNascimento = input('Digite a data de nascimento (DD/MM/AAAA): ').split('/')
dataNascimento = [int(valor) for valor in dataNascimento]

dataAtual = input('Digite a data atual (DD/MM/AAAA): ').split('/')
dataAtual = [int(valor) for valor in dataAtual]

if diaValido(*dataNascimento) and diaValido(*dataAtual):
    resultado_idade = idade(dataNascimento, dataAtual)
    if resultado_idade is not None:
        anos, meses, dias = resultado_idade
        print(f'A idade é: {anos} anos, {meses} meses e {dias} dias.')
    else:
        print('Data de nascimento maior que data atual. Verifique as datas.')
else:
    print('Data de nascimento ou data atual inválida.')
