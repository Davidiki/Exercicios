'''Calcule as raízes da equação de 2o grau.
Lembrando que: Onde 𝛥=𝑏2−4𝑎𝑐
E 𝑎𝑥2+𝑏𝑥+𝑐=0 representa uma equação de 2º grau.
A variável a tem que ser diferente de zero. Caso seja igual, imprima
a mensagem “Não é equação de segundo grau”.
• Se Δ < 0, não existe real. Imprima a mensagem “Não existe raiz”.
• Se Δ = 0, existe uma raiz real. Imprima a raiz e a mensagem
“Raiz única”.
• Se Δ ≥ 0, imprima as duas raízes reais.'''

a = float(input("Digite o coeficiente de x^2: "))
b = float(input("Digite o coeficiente de x: "))
c = float(input("Digite o termo independente: "))


if a == 0:
    print("Não é equação de segundo grau")

delta = b ** 2 - 4 * a * c

if delta < 0:
    print("Não existe raiz")

elif delta == 0:
    raiz = (-b) / (2 * a)
    print(f"Raiz única: {raiz}")

else:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"Raízes reais distintas: {raiz1}, {raiz2}")


