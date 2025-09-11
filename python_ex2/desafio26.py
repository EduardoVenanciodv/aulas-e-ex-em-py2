pa = 0
p = int(input('\033[32mDigite o primeiro termo:'))
r = int(input('Razão:\033[m '))

while pa != 10:
    print(f'\033[34m{p}', end='->')
    p += r
    pa += 1
print('\033[m Fim')
