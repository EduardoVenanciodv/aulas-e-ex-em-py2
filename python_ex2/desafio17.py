p = int(input('Digite um numero :'))
cont = 0
for c in range(1, p+1):
    if p % c == 0:
        print(f'\033[32m{c}\033[m', end=' ')
        cont += 1
    else:
        print(f'\033[31m{c}\033[m', end=' ')

print(f'\nO número {p} foi divisivel {cont} vez(es)')
if cont == 2 or cont == 1:
    print('\033[32mPor isso ele é primo!\033[m')
elif cont >= 3:
    print('\033[31mPor isso ele não é primo!\033[m')
