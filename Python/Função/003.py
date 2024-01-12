'''
Faça um programa em Python que implemente uma função INVERTE que receba
um número como parâmetro e retorne este número escrito ao contrário.
Ex: 4312 → 2134. Peça um número, chame a função e imprima o resultado.
'''

def inverte(num):
    numInv = int(str(num)[::-1])
    return numInv


x = int(input('Digite um número: '))


numInv = inverte(x)

print(f'O número invertido de {x} é {numInv}')