'''
Elabore um algoritmo que leia uma nota. Caso uma nota lida seja
inválida, emitir mensagem e repetir a entrada de dados.
'''


while True:
    nota = float(input('Digite uma nota: '))
    if 0 <= nota <= 10:
        print(f"Nota válida: {nota}")
        break
    else:
        print("Nota inválida. A nota deve estar entre 0 e 10. Tente novamente.")
