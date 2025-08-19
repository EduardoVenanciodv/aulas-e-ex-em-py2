
v = float(input('Digite o valor do produto:R$ '))

print('\033[36mDinheiro e Cheque 10% de desconto.\n'
      'Cartão Débito 5% de desconto.\n'
      'Em Duas Vezes no Cartão de credito valor normal.\n'
      'Em três vezes ou mais tem 20% de juros\033[m')

pago = int(input('\033[;32mQual é a forma de pagamento?\033[m\n\033[35m(0) dinheiro e cheque\n(1) Debido\n'
                 '(2) Em duas vezes no cartao\n'
                 '(3) em tres vezes ou mais no cartao:\033[m'))

din = (v*10) / 100
r = v - din
div2 = (v*5) / 100
r2 = v - div2
#div3 = (v*20) / 100
#r3 = v + div3

if pago == 0:
    print('\033[32mO valor do desconto de 10% é de R${:.2f} e o valor final ficara em R${:.2f}.'.format(din, r))
elif pago == 1:
    print('\033[32mO valor do desconto de %5 é de R${:.2f} e o valor final ficara em R${:.2f}\033[m'.format(div2, r2))
elif pago == 2:
    print('Em 2 vezes no cartão o valor ficara normal R${:.2f}, em 2 vezes fica {:.2f}'.format(v, v/2))
elif pago == 3:
    x1 = int(input('Vai ser parcelado em quantas vezes? '))
    div3 = (v * 20) / 100
    r3 = v + div3
    r4 = r3 / x1
    print('\033[31mVai ser em {}x de {:.2f}, tem um juros de 20%. Com um acrescimo de R${:.2f}, '
          'o valor final é de R${:.2f}\033[m'.format(x1, r4, div3, r3))
