v = 0

for c in range(1, 6+1):
    if c % 2 == 0:
        v = v + c
        #print(c)
        
print(f'\033[35mO resultado da soma dentre os seis números que são pares é:{v}\033[m')
