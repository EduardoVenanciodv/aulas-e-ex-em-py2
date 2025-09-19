pri = int(input('\033[36mDigite o primeiro termo: '))
r = int(input('Digite a razão:\033[m '))

cont = 1
mais_termos = 10
termo = pri
total = 0

while mais_termos != 0:
    total += mais_termos
    while cont <= total:
        print(f'\033[35m{termo}\033[m', end='\033[36m -> \033[m')
        termo += r
        cont += 1

    print('PAUSA')
    mais_termos = int(input('\n\033[34mDigite quantos mais termos voce quer ver dessa PA:\033[m '))

print(f'\033[31mPrograma encerrado. Com {total} termos mostrados.\033[m')
