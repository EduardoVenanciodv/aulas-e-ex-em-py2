print('\033[35mFatorial númerica.')

n = int(input('Digite um número :\033[m '))
print(f'\033[34m{n}! =\033[m ', end='')

n2 = 1
n += 1

while n != 1:
    n -= 1
    n2 *= n
    print(f'\033[36m{n}', end='x')
print(f' =\033[m {n2} ')

