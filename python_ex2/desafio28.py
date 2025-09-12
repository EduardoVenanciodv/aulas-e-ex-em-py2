n = int(input('\033[33mQuantos números você quer na sequência:\033[m '))
cont = 0
inic = 0
v = 1
while n != cont:
    cont += 1
    print(f'\033[34m{inic}\033[m', end='\033[31m->\033[m')

    soma = v + inic
    inic = v
    v = soma
