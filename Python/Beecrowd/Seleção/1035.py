A, B, C, D = map(int, input().split())

if B > C and D > A and (C+D) > (A+B) and C > 0 < D and A % 2 == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')