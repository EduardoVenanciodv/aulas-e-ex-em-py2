print('\033[35m_-_' * 10)
print('     10 TERMOS DE UMA PA')
print('_-_' * 10)

p = int(input('\033[m\033[34mDigite o primeiro termo:'))
r = int(input('Razão: '))
d = p + (11 - 1) * r

for c in range(p, d, r):
    print(c, end='->')
print(' Fim\033[m')
