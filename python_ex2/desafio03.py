
n = int(input('Digite o primeiro numero: '))
n1 = int(input('Digite o segundo numero: '))

if n > n1:
    print('{} é maior que {}.'.format(n, n1))
elif n < n1:
    print('{} é menor que {}.'.format(n, n1))
elif n == n1:
    print('{} é igual a {}.'.format(n, n1))
else:
    print('INVALIDO')
