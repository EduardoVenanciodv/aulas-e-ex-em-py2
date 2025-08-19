n = str(input('Digite seu nome: '))

if n == 'Eduardo':
    print('Seu nome é lindo!')
elif n == 'Bruno' or n == 'Jose' or n == 'Davi':
    print('Seu nome é bem feio!')
elif n in 'Luiz Laura Marcos Breno Lara':
    print('Seu nome é bem estranho!')
else:
    print('Seu nome é bem normal!')
print(f'Tenha uma boa noite, {n}.')
