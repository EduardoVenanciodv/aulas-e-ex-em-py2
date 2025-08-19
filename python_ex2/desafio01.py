
print('\033[1;35;40mBom dia. Bem vindo ao Banco bipython!\033[m')

enter = int(input('Você precisa de um emprestimo? Digite (1) para SIM ou (2) para NÃO.'))

sim = 1

if enter == sim:
    nome = str(input('Digite seu nome:'))
    sal = float(input('Digite o valor do seu salário mensal: '))
    casa = float(input('Digite quanta vai custar a casa: '))
    x = int(input('Em quantos anos você pretende pagar? '))

    par = casa / (x * 12)

    valor = (sal * 30) / 100

    #x1 = x * 12

    if par <= valor:
        print('\033[1;32mParabens, {}.'.format(nome))
        print('Emprestimo aceito\033[m')
        print('Seu emprestimo de {:.2f}R$, vai ficar parcelado por {} vezes, no valor de {:.2f} mensais.'.format(casa, x1, par))

    else:
        print('\033[1;31mInfelizmente {}'.format(nome))
        print('Seu empretimo foi Negado!\033[m')
    #print('\033[1mSeu parcelamento ficaria em {:.2f} e você pode pagar {:.2f}!\033[m'.format(par, valor))
else:
    print('Fim')



#nome = str(input('Digite seu nome:'))
#sal = float(input('Digite o valor do seu salário mensal: '))
#casa = float(input('Digite quanta vai custar a casa: '))
#x = int(input('Em quantos anos você pretende pagar? '))


#par = casa / x * 12
#valor = (sal * 30) / 100

#if par < valor:
    #print('Parabens, {}.'.format(nome))
    #print('Emprestivo aceito')

#else:
    #print('Infelizmente {}'.format(nome))
    #print('Seu empretimo foi Negado!')
#print('Seu parcelamento ficaria em{:.2f} e você pode pagar {:.2f}!'.format(par , valor))
