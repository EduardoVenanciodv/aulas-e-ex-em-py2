
frase = str(input('\033[33mDigite uma frase:\033[m')).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

print(f'\033[34mO inverso de \033[m{frase}\033[34m é \033[m{inverso}.', end='')
if frase == inverso:
    print('\033[32mA palavra digitada é um palíndromo!\033[m')
else:
    print('\033[31mA palavra digitada não é palíndromo!\033[m')
