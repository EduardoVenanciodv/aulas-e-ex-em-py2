cont = 0

while True:
    tabuada = int(input('\033[36mQuer ver a tabuada de qual valor ?\033[m'))

    print('\033[34m--\033[m'*20)
    if tabuada < 0:
        break
    for cont in range(1, 11):
        r = tabuada * cont
        print(f'{tabuada} \033[34mX\033[m {cont} \033[34m=\033[m {r}')
    print('\033[34m--\033[m' * 20)

print('\033[33mPrograma tabuada encerrado. Volte sempre!\033[m')



