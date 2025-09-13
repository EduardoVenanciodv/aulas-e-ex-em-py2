continuar = 'S'
cont = 0
r = 0
maiornumero = 0
menornumero = 0
while 'S' == continuar:
    n = int(input('\033[35mDigite um numero:\033[m'))
    if cont == 0:
        maiornumero = n
    if maiornumero < n:
        maiornumero = n

    if cont == 0:
        menornumero = n
    if menornumero > n:
        menornumero = n

    continuar = str(input('\033[34mVocê quer continuar?\033[32mS\033[m/\033[31mN\033[m')).upper()
    cont += 1
    r += n


media = r / cont

print(f'\033[31mO maior numero é o :\033[m{maiornumero}')
print(f'\033[32mO menor numero é o :\033[m{menornumero}')
print(f'\033[33mA média de todos os números é de:\033[m {media}')
