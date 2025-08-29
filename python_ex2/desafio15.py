v1 = 0
cont = 0
for c in range(1, 6+1):
    v = int(input('Digite um numero:'))
    if v % 2 == 0:
        v1 += v
        cont += 1
        
print(f'\033[35mO resultado da soma do(s) \033[m{cont}\033[35m número(s) que são pares é:{v1}\033[m')
