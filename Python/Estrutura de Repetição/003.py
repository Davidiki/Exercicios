'''
Considerando uma classe com 60 alunos, elabore um algoritmo que
leia duas notas de cada aluno, calcule a média e verifique se
aluno foi aprovado ou reprovado. Para estar aprovado a média
deverá ser maior ou igual a 6. Determine também a média geral da
classe e a quantidade de alunos aprovados e reprovados da turma.

'''

aluno = 1
medias = 0
aprovados = 0
reprovados = 0

while aluno <= 10:
    nota1 = float(input(f'1º Nota do aluno {aluno}: '))
    nota2 = float(input(f'2º Nota do aluno {aluno}: '))
    media = (nota1 + nota2) / 2
    medias += media
    if media < 6:
        print(f'Aluno {aluno} Reprovado')
        reprovados += 1
    else:
        print(f'Aluno {aluno} Aprovado')
        aprovados += 1
    aluno += 1
mediaGeral = medias / 10

print(f'Alunos aprovados: {aprovados}\n'
      f'Alunos Reprovados: {reprovados}\n'
      f'Média geral da turma: {mediaGeral}')