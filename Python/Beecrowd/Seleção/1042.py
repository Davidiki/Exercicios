a,b,c = map(int,input().split())

menor = min(a,b,c)
maior = max(a,b,c)

if a != menor and a != maior:
    medio = a
elif b != menor and b != maior:
    medio = b
else:
    medio = c



print(f'{menor}\n'
      f'{medio}\n'
      f'{maior}\n')

print(f'{a}\n'
      f'{b}\n'
      f'{c}')
