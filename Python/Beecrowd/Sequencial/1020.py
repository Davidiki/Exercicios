data = int(input())

ano = data // 365
data -= ano * 365
meses = data // 30
dias =  data % 30

print(f'{ano} ano(s)\n'
      f'{meses} mes(es)\n'
      f'{dias} dia(s)')