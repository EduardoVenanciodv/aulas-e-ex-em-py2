v = 0 
cont = 0
for c in range(1 , 500+1, 2):
    if c % 3 == 0:
        v = v + c
        cont = cont + 1
        
print(f'\033[33mA somas dos \033[m{cont}\033[33m valores múltiplos por 3 deu:\033[m {v}')
