n1, n2, n3, n4 = map(float, input().split())
media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + n4) / 10

if media >= 7:
    print(f'Media: {media:.1f}\n'
          f'Aluno aprovado.')
elif media < 5:
    print(f'Media: {media:.1f}\n'
          f'Aluno reprovado.')
else:
    n5 = float(input())
    mediaFinal = (media + n5) / 2
    print(f'Media: {media:.1f}\n'
          f'Aluno em exame.\n'
          f'Nota do exame: {n5:.1f}')
    if mediaFinal >= 5:
        print(f'Aluno aprovado.\n'
              f'Media final: {mediaFinal:.1f}')
    else:
        print(f'Aluno reprovado.\n'
              f'Media final: {mediaFinal:.1f}')

