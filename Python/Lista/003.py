'''
Elabore um algoritmo que crie um vetor capaz de armazenar os 20
primeiros valores ímpares.
'''

vetor = []
cont = 0
impar = 0

while len(vetor) < 20:
    if cont % 2 != 0:
        vetor.append(cont)
    cont += 1

print(vetor)