cont = 0
print('Gerador de PA')
p = int(input('\033[32mDigite o primeiro termo:'))
r = int(input('Razão:\033[m '))

while cont != 10:
    print(f'\033[34m{p}', end='->')
    p += r
    cont += 1
print('\033[m Fim')
