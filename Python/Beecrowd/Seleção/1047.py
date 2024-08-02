horaInicial, minutoInicial, horaFinal, minutoFinal = map(int, input().split())

duracao_minutos = (horaFinal * 60 + minutoFinal) - (horaInicial * 60 + minutoInicial)

if duracao_minutos <= 0:
    duracao_minutos += 24 * 60

horas = duracao_minutos // 60
minutos = duracao_minutos % 60

print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')
