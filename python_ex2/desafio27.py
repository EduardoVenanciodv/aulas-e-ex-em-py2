pa = 0
t = 10
pri = int(input('\033[36mDigite o primeiro termo: '))
r = int(input('Digite a razão:\033[m '))

while pa != t:
    if t >= 10:
        print(f'\033[35m{pri}\033[m', end='\033[36m -> \033[m')
        pri += r
        pa += 1

    if pa >= t:
        t = int(input('\n\033[34mDigite quantos mais termos voce quer ver dessa PA:\033[m '))+t

print('\033[31mPrograma encerrado\033[m')
