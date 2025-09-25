print('\033[35m/|\\\033[m'*11)
print('\033[35m/|\\/|\\/|\\/|\\\033[34mBANCO DV\033[35m/|\\/|\\/|\\/|\\\033[m')
print('\033[35m/|\\\033[m'*11)
sacar = int(input('\033[34mQual o valor que você quer sacar?\033[m \033[35mR$\033[m'))
total = sacar
ced = 50
contced = 0
while True:
    if total >= ced:
        total -= ced
        contced += 1
    else:
        if contced > 0:
            print(f'\033[34mTotal de \033[35m{contced}\033[34m cédulas de \033[35mR${ced}\033[m')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        contced = 0
        if total == 0:
            break
print('\033[35m/|\\\033[m'*11)
print('\033[34mVolte sempre ao BANCO DV!\033[m')
