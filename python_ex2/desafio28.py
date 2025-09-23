print('Sequência de Fibonacci')

n = int(input('\033[33mQuantos números você quer na sequência:\033[m '))
cont = 1
t1 = 0
t2 = 1
while cont <= n:
    t3 = t1 + t2
    print(f'\033[34m{t1}\033[m', end='\033[31m->\033[m')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
