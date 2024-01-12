'''4.) Faça um algoritmo que leia dois valores inteiros e
positivos e armazene nas variáveis A e B respectivamente.
Em seguida troque o conteúdo das variáveis, ou seja, A deverá
receber o valor de B e B o valor de A.
'''

a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))

c = a
a = b
b = c

print(f'O valor de A: {a}\n'
      f'O valor de B: {b}')
