'''1.) Elabore um algoritmo que leia duas notas, calcule a
média e verifique se aluno foi aprovado ou reprovado. Para estar
aprovado a média deverá ser maior ou igual a 6.
'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media >= 6:
    print(f'Média: {media}\n'
          f'Aluno aprovado')
else:
    print(f'Média: {media}\n'
          f'Aluno reprovado')