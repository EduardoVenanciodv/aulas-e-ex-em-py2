con = 0
f = 'feminino'
for c in range(1 , 4+1):
    nome = str(input('\033[33mDigite seu nome: \033[m'))
    idade = int(input('\033[33mDigite sua idade: \033[m'))
    sexo = str(input('\033[33mDigite seu sexo: \033[m'))
    if c == 1:
        i = idade + 0
        n = nome
        s = sexo
        if s == f and i < 20:
            con += 1
        
    elif c == 2:
        i2 = idade + 0
        n2 = nome
        s2 = sexo
        if s2 == f and i2 < 20:
            con += 1
            
    elif c == 3:
        i3 = idade + 0
        n3 = nome
        s3 = sexo
        if s3 == f and i3 < 20:
            con += 1
        
    elif c == 4:
        i4 = idade + 0
        n4 = nome
        s4 = sexo
        if s4 == f and i4 < 20:
            con += 1
        
m = (i + i2 + i3 + i4)/4
print(f'\033[34mA média de idade de todos é:\033[m{m}')

m2 = 'masculino'
if  i > i2 and i > i3 and i > i4 and s == m2:
    print(f'\033[34mO Homem Mais velho é o \033[m{n}\033[34m, com \033[m{i} anos.')
elif s2 == m2 and i2 > i and i2 > i3 and i2 > i4:
    print(f'\033[34mO Homem Mais velho é o \033[m{n2}\033[34m, com \033[m{i2} anos.')
elif s3 == m2 and i3 > i and i3 > i2 and i3 > i4:
    print(f'\033[34mO Homem Mais velho é o \033[m{n3}\033[34m, com \033[m{i3} anos.')
elif s4 == m2 and i4 > i and i4 > i2 and i4 > i3:
    print(f'\033[34mO Homem Mais velho é o \033[m{n4}\033[34m, com \033[m{i4} anos.')

if con >= 1:
    print(f'\033[34mExiste \033[m{con}\033[34m mulher(es) com menos de \033[m20 anos.')
