'''
5.) Escreva um algoritmo que leia um tempo em segundos e calcule o
total de horas, minutos e segundos  equivalentes a este tempo dado
de entrada.
	Por exemplo:

7850 segundos é igual a:  2 horas 10 minutos e 50 segundos.
'''

segundos = int(input('Tempo em segunos: '))

horas = segundos // 3600
segundos %= 3600
minutos = segundos // 60
segundos %= 60

print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")