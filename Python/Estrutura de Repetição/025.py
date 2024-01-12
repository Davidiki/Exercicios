'''
Faça um programa que leia vários números, calcule e mostre:
(a) A soma dos números digitados
(b) A quantidade de números digitados
(c) A média dos números digitados
(d) O maior numero digitado
(e) O menor número digitado
(f) A média dos números pares
Finalize a entrada de dados caso o usuário informe o valor 0
'''

num = int(input('Digite um número [Digite 0 para finalizar]: '))
soma = 0
cont = 0
maior = 0
menor = num
mediaPar = 0

while True:
    num = int(input('Digite outro número[Digite 0 para finalizar]: '))
    soma += num
    cont += 1
    if num > maior:
        maior = num
    if num < menor and num != 0:
        menor = num
    if num % 2:
        mediaPar += 1
    if num == 0:
        break

media = soma / cont

print(f'A soma dos números digitados {soma}\n'
      f'A quantidade de números digitados {cont}\n'
      f'A média dos números digitados {media}\n'
      f'O maior numero digitado {maior}\n'
      f'O menor número digitado {menor}\n'
      f'A média dos números pares {mediaPar}')

