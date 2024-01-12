'''
Elabore um algoritmo que leia um número inteiro e o inverta.
Veja alguns exemplos:

Num = 1234  Invertido = 4321
Num = 564378  Invertido = 873465

'''

num = int(input("Digite um número inteiro: "))

inv = 0

while num > 0:
    digito = num % 10
    inv = inv * 10 + digito
    num //= 10

print(f"O número invertido é: {inv}")
