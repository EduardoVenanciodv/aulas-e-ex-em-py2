
n = int(input('Digite um numero:'))

n1 = int(input('Você quer que esse numero seja:\n(1) binário\n'
               '(2) octal\n(3) hexadecimal\n'))

bina = 1
octa = 2
hexa = 3

if n1 == 1:
    print('Convertido para binário:{}'.format(bin(n)[2:]))
elif n1 == 2:
    print('Convertido para octal:{}'.format(oct(n)[2:]))
elif n1 == 3:
    print('Convertido para hexadecimal:{}'.format(hex(n)[2:]))
else:
    print('Não foi escolhido as opções citadas! Reinicie a programa.')

print(f'{n}')
