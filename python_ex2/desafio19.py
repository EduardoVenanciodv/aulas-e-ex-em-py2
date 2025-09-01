from datetime import date

total1 = 0
total2 = 0

for c in range(1, 8):
    nascimento = int(input(f'Digite a data da {c}^ de náscimento:'))
    ano = date.today().year
    idade = ano - nascimento

    if idade >= 21:
        #print('\033[31mVocê é maior de idade.\033[m')
        total1 = total1 + 1
    elif idade >= 0:
        #print('\033[32mVocê é menor de idade.\033[m')
        total2 = total2 + 1
    else:
        print('Erro (-)')
print('\033[35mTemos {} maior de idade e {} Menor de idade.\033[m'.format(total1, total2))

