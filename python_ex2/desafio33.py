from random import randint

cont = 0
print('\033[32m/\033[33m|\033[31m\\\033[m' * 10)
print('\033[33mVAMOS JOGAR ÍMPAR OU PAR\033[m')
print('\033[32m/\033[33m|\033[31m\\\033[m' * 10)
while True:
    eu = int(input('\033[33mDigite um valor:\033[m'))
    computador = randint(0, 10)
    r = computador + eu
    pi = ' '
    while pi not in 'PpIi':
        pi = str(input('\033[33mPar ou Ímpar (P/I):\033[m')).upper().strip()[0]
    if r % 2 == 0:
        print(f'\033[33mVocê jogou \033[m{eu}\033[33m e o computador \033[m{computador}\033[33m. '
              f'Total de \033[m{r}\033[33m deu PAR\033[m')
        if pi == 'P':
            print('\033[32mVocê ganhou!!')
            print('Vamos novamente...\033[m')
            print('--' * 20)
            cont += 1
        else:
            print('\033[31mVocê Perdeu!\033[m')
            print('--' * 20)
            break
    else:
        print(f'\033[33mVocê jogou \033[m{eu}\033[33m e o computador \033[m{computador}\033[33m. '
              f'Total de \033[m{r}\033[33m deu Ímpar\033[m')
        if pi == 'I':
            print('\033[32mVocê ganhou!!')
            print('Vamos novamente...\033[m')
            print('--' * 20)
            cont += 1
        else:
            print('\033[31mVocê Perdeu!\033[m')
            print('--' * 20)
            break

print(f'\033[31mGamer OVER!\033[33m \033[32mVocê ganhou \033[m{cont}\033[32m vez(es).')
