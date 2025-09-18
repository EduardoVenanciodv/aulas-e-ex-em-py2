print('\033[35mFatorial númerica.')

n = int(input('Digite um número :\033[m '))
print(f'\033[34m{n}! =\033[m ', end='')

c = n
f = 1

while c > 0:
    print(f'\033[36m{c}', end=' ')
    print(' x ' if c > 1 else '=', end=' ')
    f *= c
    c -= 1
print(f'\033[m{f} ')

