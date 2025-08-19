from datetime import date
d = date.today().year

i = int(input('Digite o ano de nascimento:'))

r = d - i

if r <= 9:
    print('Classificação: MIRIM')
elif r <= 14:
    print('Classificação: Infantil')
elif r <= 19:
    print('Classificação: Junior')
elif r <= 25:
    print('Classificação: Sênior')
else:
    print('Classificação: Master')
print(f'{r} Anos')
