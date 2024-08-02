a, b = map(int, input().split())
if a > b:
    tempo = (24 - a) + b
if a == b:
    tempo = 24
if a < b:
    tempo = b - a
print(f'O JOGO DUROU {tempo} HORA(S)')