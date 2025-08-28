us = int(input('\033[34mDigite um número para ver sua tabuada: \033[m'))
c1 = 0

print('\033[34m=*=\033[m'*10)
print(f'\033[35mTabuada de {us}.\n')
for c in range (1 , 10+1):  
    print('{} X {} = {}'.format(us, c , c*us))
print('\033[34m=*=\033[m'*10)
