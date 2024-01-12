'''
Elabore um programa que leia um vetor capaz de armazenar 10 números e
em seguida, leia um valor e verifique se este valor existe ou não no
vetor lido. Caso ele exista, indique quantas vezes ele aparece no vetor.
'''

from random import randint
vetor = []

for i in range(10):
    vetor.append(randint(1, 100))

num = int(input('Digite um número e descubra se ele existe no vetor: '))

if num in vetor:
    print(f'{num} existe no vetor')
else:
    print(f'{num} não existe no vetor')