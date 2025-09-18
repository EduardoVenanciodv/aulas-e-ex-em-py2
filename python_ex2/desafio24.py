from time import sleep

v1 = int(input('Digite o primeiro valor:'))
v2 = int(input('Digite o segundo valor:'))
opc = 0

print('\033[33mInicio\033[m')
while opc != 5:

    opc = int(input('\033[33mEscola umas das opções abaixo:\033[m\n'
                    '[1]SOMA\n[2]MULTIPLICAR\n[3]MAIOR\n'
                    '[4]NOVOS NÚMEROS\n[5]SAIR DO PROGRAMA\n'))

    if opc == 1:
        r = v1 + v2
        print(f'\033[34mA soma de ({v1} + {v2}) =\033[m {r}')
    elif opc == 2:
        r = v1 * v2
        print(f'\033[34mA multiplicação de ({v1} X {v2}) =\033[m {r}')

    elif opc == 3:
        if v1 > v2:
            print(f'\033[34mO Maior número é o primeiro digitado:\033[m {v1}')
        elif v1 < v2:
            print(f'\033[34mO Maior número é o segundo digitado:\033[m {v2}')
        else:
            print(f'\033[34mOs números são iguais:\033[m {v1} | {v2}')
    elif opc == 4:
        print('\033[33mInforme os números novamente:\033[m ')
        v1 = int(input('Digite o primeiro valor:'))
        v2 = int(input('Digite o segundo valor:'))
    elif opc == 5:
        print('\033[36mFinalizando...\033[m')
        sleep(1.3)
    else:
        print('\033[31mErro!!\nEssa opção não existe!!\033[m')
    print('\033[36m-*-\033[m' * 13)
print('\033[33mFim\033[m')
