horario = int(input())

hora = horario // 3600
horario -= hora * 3600
minuto = horario // 60
segundos = horario % 60

print(f'{int(hora)}:{int(minuto)}:{segundos}')