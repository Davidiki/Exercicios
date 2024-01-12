'''
Elabore um algoritmo que leia dois vetores de 10 valores cada e calcule
o produto escalar entre eles:

PE =  A[0]*B[0] + A[1]*B[1] + A[2]*B[2] + A[3]*B[3] + ... + A[9]*B[9]
'''
from random import randint

vetor1 = []
vetor2 = []
vetor3 = []

for i in range(10):
    vetor1.append(randint(1, 100))
    vetor2.append(randint(1, 100))
    vetor3.append(vetor1[i] * vetor2[i] )
print(f'{vetor1}\n'
      f'{vetor2}\n'
      f'{vetor3}')