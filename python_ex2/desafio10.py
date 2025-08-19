from random import randint
from time import sleep
print('-=' * 12)
eu1 = int(input('\033[36mDigite:\n(0) pedra\n(1) papel\n(2) tesoura:\033[m'))

#pedra = 0
#papel = 1
#tesoura = 2
r = ['PEDRA', 'PAPEL', 'TESOURA']
r1 = randint(0, 2)

print('-=' * 12)
print('JO')
sleep(1)
print('   KEN')
sleep(1)
print('      PO!')
print('-=' * 12)

print('\033[35mVocê escolheu:{}\nComputador escolheu:{}\033[m'.format(r[eu1], r[r1]))
print('-=' * 12)
if eu1 == 0 and r1 == 2 or eu1 == 1 and r1 == 0 or eu1 == 2 and r1 == 1:
    print('\033[32mParabéns, Você ganhou!\033[m')

elif eu1 == 2 and r1 == 0 or eu1 == 0 and r1 == 1 or eu1 == 1 and r1 == 2:
    print('\033[31mVocê perdeu!\033[m')

elif eu1 == r1:
    print('\033[37mEMPATE!\033[m')

else:
    print('\033[34mINVALIDO')
print('-=' * 12)
