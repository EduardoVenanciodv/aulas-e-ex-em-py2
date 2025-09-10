from random import randint
from time import sleep

pc = randint(0, 10)

print('\033[35m^_-' * 12)
print('Vou pensar em um número de 0 ao 10.')
print('^_-' * 12)

sleep(1)
print('\033[mLoad.')
sleep(0.7)
print('Load..')
sleep(0.5)
print('Load...')

eu = 11
tentativas = 0
while eu != pc:
    eu = int(input('\033[36mDigite seu numero:'))
    tentativas += 1

print(f'\033[36mVocê acertou é o número: \033[m{eu}\n\033[36mNúmero de tentavias:\033[m {tentativas}')
