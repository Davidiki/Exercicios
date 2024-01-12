'''
Elabore um algoritmo que leia um vetor de 10 caracteres
(a, b, c, d ou e) que é o gabarito de uma prova de múltipla escolha
aplicada a vários candidatos. Em seguida leia o vetor resposta de cada
candidato (também um vetor de 10 caracteres) e mostre a nota resultante
do candidato (0 a 10).  Repita o processo enquanto existir candidato
para ser avaliado.
'''

gabarito = ['a', 'd', 'e', 'c', 'c', 'a', 'b', 'e', 'b', 'a']

while True:
    resposta_candidato = input("Digite as respostas do candidato (10 caracteres - a, b, c, d ou e): ").lower()

    # Verifica se a resposta do candidato tem o tamanho correto
    if len(resposta_candidato) != 10 or any(resp not in 'abcde' for resp in resposta_candidato):
        print("Resposta inválida. Por favor, digite novamente.")
        continue

    # Calcula a nota do candidato sem usar zip
    nota_candidato = 0
    for i in range(10):
        if gabarito[i] == resposta_candidato[i]:
            nota_candidato += 1

    print(f"A nota do candidato é: {nota_candidato}/10")

    continuar = input("Deseja avaliar outro candidato? (s/n): ").lower()
    if continuar != 's':
        break
