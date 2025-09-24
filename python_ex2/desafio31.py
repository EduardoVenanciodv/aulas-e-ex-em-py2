n = s = cont = 0

while True:
    n = int(input('\033[33mDigite um número (999para parar):\033[m'))
    if n == 999:
        break
    cont += 1
    s += n
print(f'\033[34mForam digitados \033[33m{cont}\033[34m números, e a soma entre eles foi de \033[33m{s}')
