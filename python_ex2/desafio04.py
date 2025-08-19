from datetime import date

ano = int(input('Digite o ano do seu náscimento: '))

n = date.today().year

r = n - ano

print('Você nasceu em {}, tem {} anos em {}.'.format(ano, r, n))
if r == 17 or r == 18:
    print('Você precisa se alistar ao exercito Brasileiro!')
elif r < 17:
    valor = 17 - r
    print('Você precisa se alistar daqui há {} anos.'.format(valor))
    valor2 = valor + n
    print('Seu ano de alistamento:{}.'.format(valor2))
elif r == 19:
    print('Já está passando do seu prazo de alistamento. Vá agora há um posto de alistamento, URGENTEMENTE!')
else:
    valor = r - 19
    print('Já passou {} anos do seu prazo para se alistarse'.format(valor))
    valor2 = n - valor
    print('O seu ano de alistamento foi em:{}.'.format(valor2))
