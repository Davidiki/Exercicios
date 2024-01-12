'''
Faça um programa em Python que leia uma String e dois caracteres.
Troque todas as ocorrências do primeiro caractere (podendo ser
maiúsculo ou minúsculo) pelo segundo e imprima a quantidade de vezes
que o caractere foi substituído.
'''

frase = input('Digite uma frase: ')
caracter1 = input('Digite o primeiro caracter: ')
caracter2 = input('Digite o segundo caracter: ')
troca = 0

nova_frase = ""
for char in frase:
    if char.lower() == caracter1.lower():  # Comparação insensível a maiúsculas/minúsculas
        nova_frase += caracter2
        troca += 1
    else:
        nova_frase += char

print(f'Frase modificada: {nova_frase}')
print(f'Quantidade de vezes que o caractere foi substituído: {troca}')
