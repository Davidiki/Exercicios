'''
Elabore um algoritmo para resolver uma operação aritmética escolhida
pelo usuário. Para isto, leia operador  (+, *, -, / ou #).
O caractere # será usado para encerrar o programa. Em seguida,
leia dois operandos (números reais).O algoritmo deverá realizar a
operação escolhida entre os valores lidos.
'''


while True:
    operador = input("Digite um operador (+, *, -, /) ou '#' para encerrar: ")

    if operador == '#':
        break

    num1 = int(input("Digite o primeiro operando: "))
    num2 = int(input("Digite o segundo operando: "))

    if operador == '+':
        resultado = num1 + num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '/':
        if num2 == 0:
            print("Erro: Divisão por zero.")
            continue
        resultado = num1 / num2

    print(f"Resultado da operação: {resultado}")
