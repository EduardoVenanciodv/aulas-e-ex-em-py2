n1 = 0
n = 0
cont = 0
while n != 999:
    n = int(input('\033[36mDigite um numero qualquer. encerre o programa com (999):\033[m'))
    if n != 999:
        cont += 1
        n1 += n
print(f'\033[34mA quantidade de vezes que o usuário digitou um número é de:\033[m {cont} Vezes.\n'
      f'\033[34mA soma de todos os números exeto (999) digitados pelo usuário foi de :\033[m {n1}')

