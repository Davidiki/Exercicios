a, b, c = sorted(map(float, input().split()), reverse=True)

if a >= b + c:
    print('NAO FORMA TRIANGULO')
else:
    if a**2 == (b**2) + (c**2):
        print('TRIANGULO RETANGULO')
    if a**2 > (b**2) + (c**2):
        print('TRIANGULO OBTUSANGULO')
    if a**2 < (b**2) + (c**2):
        print('TRIANGULO ACUTANGULO')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    if (a == b != c) or (b == c != a) or (c == a != b):
        print('TRIANGULO ISOSCELES')