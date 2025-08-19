n1 = int(input('Digite o tamanho da primeira reta:'))
n2 = int(input('Digite o tamanho da segunda reta: '))
n3 = int(input('Digite o tamanho da terceira reta: '))

if n1 + n3 > n2 and n2 + n1 > n3 and n3 + n2 > n1:
    print('OS segmentos de retas formam um TRIANGULO.')
    if n1 == n2 and n2 ==n3:
        print('Do tipo: Equilátero')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('Do tipo: Isósceles')
    elif n1 < n2 or n1 > n2 and n1 < n3 or n1 > n3 and n2 < n3 or n2 > n3:
        print('Do tipo: Escaleno')
else:
    print('NAO é um TRIANGULO')
