'''
 Elabore um algoritmo que leia um número e  calcule a soma dos número
 menores ou iguais a ele, começando pelo 1.
Ex. para num == 10, o algoritmo devera
calcular: 1+2+3+4+5+6+7+8+9+10= 55

'''

num = int(input('Digite um número: '))
cont = 1
soma = 0

while cont <= num:
    soma += cont
    cont += 1

print(soma)
