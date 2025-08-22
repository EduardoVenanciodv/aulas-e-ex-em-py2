us = int(input('\033[34mDigite um número: \033[m'))
c1 = 0

print('\033[34m=*=\033[m'*10)
print(f'\033[35mTabuada de {us}.\n')
for c in c1 or range (1 , 10+1) or (1 , 10+1):
    c = c * us
    c1 = c1 + 1
    #print(c1)
    print(f'{us} X {c1} = {c}')
print('\033[34m=*=\033[m'*10)
