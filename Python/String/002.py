'''
Faça um programa em Python que leia uma frase e imprima quantas vogais
tem esta frase. Considerar minúscula e maiúscula.
'''

vogais = ['a', 'e', 'i', 'o', 'u', 'á', 'â', 'ã', 'é', 'í', 'ó', 'ô', 'ú', ]

vogal = 0
consoante =  0

frase = input('Digite uma frase: ').lower()

for char in frase:
    if char.isalpha():
        if char in vogais:
            vogal += 1
        else:
            consoante += 1

print(f'Quantidade de vogais: {vogal}\n'
      f'Quantidade de consoantes: {consoante}')
