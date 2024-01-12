'''Leia uma data e determine se ela é válida. Ou seja,
verifique se o mês está entre 1 e 12, e se o dia existe naquele mês.
Note que Fevereiro tem 29 dias em anos bissextos, e 28 dias
em anos não bissextos.'''


# Solicita ao usuário para digitar o dia, mês e ano
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

# Verifica se o mês está entre 1 e 12
if 1 <= mes <= 12:
    # Verifica se o ano é bissexto e atualiza a quantidade de dias em fevereiro
    bissexto = ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

    # Define a quantidade de dias em fevereiro
    if bissexto:
        dias_em_fevereiro = 29
    else:
        dias_em_fevereiro = 28

    # Verifica se o dia está dentro do intervalo adequado para o mês
    if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and 1 <= dia <= 31:
        print("A data é válida.")
    elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and 1 <= dia <= 30:
        print("A data é válida.")
    elif mes == 2 and 1 <= dia <= dias_em_fevereiro:
        print("A data é válida.")
    else:
        print("A data é inválida.")
else:
    print("A data é inválida.")
