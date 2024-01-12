'''A nota final de um estudante é calculada a partir de
três notas atribuídas entre o intervalo de 0 até 10, respectivamente,
a um trabalho de laboratório, a uma avaliação semestral e a um
exame final. A média das três notas mencionadas anteriormente
obedece aos pesos: Trabalho de Laboratório: 2; Avaliação Semestral:
3; Exame Final: 5. De acordo com o resultado, mostre na tela se o
aluno está reprovado (média entre 0 e 2.9), de recuperação
(entre 3 e 4.9) ou se foi aprovado. Faça todas
as verificacões necessárias.'''

n1 = float(input('Nota do trabalho de laboratório: '))
n2 = float(input('Nota da avaliação semestral: '))
n3 = float(input('Nota de exame final: '))

notaFinal = ((n1 * 2) + (n2 * 3) + (n3 * 5))  / 10
print(f'Nota final: {notaFinal}')
if notaFinal <= 2.9:
    print('Aluno Reprovado')
elif notaFinal >= 3 and notaFinal < 5:
    print('Aluno de recuperaçao')
elif notaFinal >= 5:
    print('Aluno Aprovado')