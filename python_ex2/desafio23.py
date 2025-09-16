from random import randint

pc = randint(0, 10)

print('\033[35m^_-' * 12)
print('Sou seu computador.\nVou pensar em um número de 0 ao 10.')
print('^_-' * 12)

acertou = False
tentativas = 0

while not acertou:
    eu = int(input('\033[36mQual é o seu palpite?\033[m'))

    tentativas += 1
    if eu == pc:
        acertou = True
    if eu < pc:
        print('Mais... \033[31mTentes outra vez.\033[m')
    elif eu > pc:
        print('Menos... \033[31mTentes outra vez.\033[m')

print(f'\033[32mVocê acertou é o número: \033[m{eu}\n'
      f'\033[32mNúmero de tentavias:\033[m {tentativas}\n\033[32mParabéns!!\033[m')
