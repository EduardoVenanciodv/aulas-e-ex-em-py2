continuar = 'S'
cont = 0
r = 0
maiornumero = 0
menornumero = 0
while 'S' == continuar:
    n = int(input('\033[35mDigite um número:\033[m'))
    continuar = str(input('\033[34mVocê quer continuar?\033[32mS\033[m/\033[31mN\033[m')).upper().strip()[0]
    while continuar != 'S' and continuar != 'N':
        print('\033[31mErro! Você precisa digitar umas nas opções mostradas!\033[m')
        n = int(input('\033[35mDigite um número novamente:\033[m'))
        continuar = str(input('\033[34mVocê quer continuar?\033[32mS\033[m/\033[31mN\033[m')).upper().strip()[0]
        print('\033[33m~~\033[m'*18)

    if cont == 0:
        maiornumero = menornumero = n
    else:
        if n > maiornumero:
            maiornumero = n
        if n < menornumero:
            menornumero = n
    cont += 1
    r += n
media = r / cont

print(f'\033[31mO maior numero é o :\033[m{maiornumero}')
print(f'\033[32mO menor numero é o :\033[m{menornumero}')
print(f'\033[33mVocê digitou \033[m{cont}\033[33m número(s) e a média de todos é de:\033[m {media}')
