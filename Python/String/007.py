'''
Elabore um programa em Python que lê uma String e calcule e imprima um
código utilizando a seguinte regra: para cada vogal, somar 5 pontos,
para cada consoante somar 10 pontos, desconsiderando qualquer outro
caractere. Exemplo: Linguagem de Programação 10 vogais (lembre-se de
considerar vogais acentuadas) → 10 x 5 = 50
12 consoantes → 12 x 10 = 120 Código = 170
'''

frase = input('Digite uma palavra ou uma frase: ')
vogal = 0
consoante = 0

for i in range(len(frase)):
    if frase[i] != frase.isspace():
        if frase[i] in 'aAãÃâÂáÁeéEÉiIíÍoOóÓôÔuUúÚ':
            vogal += 5
        else:
            consoante += 10

print(f'{frase}\n'
      f'{vogal} + {consoante} = {vogal + consoante} ')