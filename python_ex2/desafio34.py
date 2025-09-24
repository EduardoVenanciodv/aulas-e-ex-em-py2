mais18 = homens = mulher20 = 0
print('--' *15)
print('     \033[34mCADASTRE UMA PESSOA\033[m')
print('--' *15)

while True:
    sexo = ''
    continuar = ''

    idade = int(input('\033[34mDigite sua idade:\033[m'))
    if idade > 18:
        mais18 += 1
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('\033[34mDigite seu sexo (M/F):\033[m')).upper().strip()[0]
        if sexo == 'M':
            homens += 1
        if sexo == 'F' and idade < 20:
            mulher20 += 1
    print('--' * 15)
    while continuar != 'S' and continuar != 'N' :
        continuar = str(input('\033[36mQuer continuar?(S/N)\033[m')).upper().strip()[0]
    print('--' * 15)
    if continuar == 'N':
        break
print('\033[35m=====--|FIM DO PROGRAMA|--=====\033[m')
print(f'\033[34mTem \033[m{mais18}\033[34m pessoas com mais de 18 anos.\033[m')
print(f'{homens} \033[34mHomens foram cadastrados.\033[m')
print(f'{mulher20} \033[34mMulheres que foram cadastradas tem menos de 20 anos.\033[34m')
