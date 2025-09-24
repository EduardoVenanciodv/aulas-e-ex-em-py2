cont50 = cont20 = cont10 = cont1 = 0
print('\033[35m/|\\\033[m'*11)
print('\033[35m/|\\/|\\/|\\/|\\\033[34mBANCO DV\033[35m/|\\/|\\/|\\/|\\\033[m')
print('\033[35m/|\\\033[m'*11)
sacar = int(input('\033[34mQual o valor que você quer sacar?\033[m \033[35mR$\033[m'))

while True:
    if sacar >= 50:
        sacar -= 50
        cont50 += 1
    elif sacar >= 20 and sacar < 50:
        sacar -= 20
        cont20 += 1
    elif sacar >= 10 and sacar < 20:
        sacar -= 10
        cont10 += 1
    elif sacar >= 1 and sacar < 10:
        sacar -= 1
        cont1 += 1
    else:
        break
print(f'\033[34mTotal de \033[35m{cont50}\033[34m cédulas de \033[35mR$50\033[m')
print(f'\033[34mTotal de \033[35m{cont20}\033[34m cédulas de \033[35mR$20\033[m')
print(f'\033[34mTotal de \033[35m{cont10}\033[34m cédulas de \033[35mR$10\033[m')
print(f'\033[34mTotal de \033[35m{cont1}\033[34m cédulas de \033[35mR$1\033[m')
print('\033[35m/|\\\033[m'*11)
print('\033[34mVolte sempre ao BANCO DV!\033[m')
