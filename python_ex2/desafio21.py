mulher20 = 0
media = 0
somadaidade = 0
maioridade = 0
nomevelho = ''

for c in range(1, 4+1):
    print(f'\033[34m*****\033[m {c}^ Pessoa \033[34m*****\033[m')
    nome = str(input('\033[33mNome: \033[m')).strip()
    idade = int(input('\033[33mIdade: \033[m'))
    sexo = str(input('\033[33mSexo[m/f]: \033[m')).strip()
    somadaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridade = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and maioridade < idade:
        maioridade = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1
    media = somadaidade / 4
print(f'\033[34mA média de idade de todos é:\033[m{media}')
print(f'\033[34mO homem mais velho é o \033[m{nomemaisvelho}\033[34m com \033[m{maioridade}\033[34m anos.\033[m')
print(f'\033[34mExiste \033[m{mulher20}\033[34m mulher(es) com menos de \033[m20 anos.')
