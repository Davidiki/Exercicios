A, B, C = map(float, input().split())

triangulo = (1/2) * A * C
circulo = (3.14159) * C**2
trapezio = (1/2) * (A + B) * C
quadrado = B * B
retangulo = A * B

print(f'TRIANGULO: {triangulo:.3f}\n'
      f'CIRCULO: {circulo:.3f}\n'
      f'TRAPEZIO: {trapezio:.3f}\n'
      f'QUADRADO: {quadrado:.3f}\n'
      f'RETANGULO: {retangulo:.3f}')