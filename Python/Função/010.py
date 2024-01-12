'''
Faça um programa que calcule as raízes da equação de 2o grau.
Lembrando que:
Onde 𝛥=𝑏2−4𝑎𝑐
E 𝑎𝑥2+𝑏𝑥+𝑐=0 representa uma equação de 2º grau.
A variável a tem que ser diferente de zero. Caso seja igual, imprima a
mensagem “Não é equação de segundo grau”.
• Se Δ < 0, não existe real. Imprima a mensagem “Não existe raiz”.
• Se Δ = 0, existe uma raiz real. Imprima a raiz e a mensagem “Raiz única”.
• Se Δ ≥ 0, imprima as duas raízes reais.
Faça funções para o cálculo do delta e das raízes.
'''


def calculaDelta(a, b, c):
    return b ** 2 - 4 * a * c


def calculaRaizes(a, b, c):
    delta = calculaDelta(a, b, c)

    if a == 0:
        return 'Não é equação de segundo grau'
    elif delta == 0:
        raiz = -b / (2 * a)
        return f'Raiz única: {raiz}'
    elif delta > 0:
        raiz1 = (-b + (delta ** 0.5)) / (2 * a)
        raiz2 = (-b - (delta ** 0.5)) / (2 * a)
        return f'Raízes reais: {raiz1} e {raiz2}'
    else:
        return 'Não existe raiz real'


a = float(input('Digite o coeficiente a: '))
b = float(input('Digite o coeficiente b: '))
c = float(input('Digite o coeficiente c: '))

resultado = calculaRaizes(a, b, c)
print(resultado)
