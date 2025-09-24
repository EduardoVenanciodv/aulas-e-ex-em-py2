soma = menor_valor = maior1000 = 0

print('--'*15)
print('=-----LOJA DO GAFANHOTO-----=')
print('--'*15)
while True:
    produto = str(input('Nome do produto:'))
    valor = int(input('Valor: '))
    soma += valor
    if valor > 1000:
        maior1000 += 1
    if menor_valor == 0:
        menor_valor = valor
        produto_barato = produto
    if valor < menor_valor:
        menor_valor = valor
        produto_barato = produto
    continuar = ''
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar comprando (S/N):')).upper().strip()[0]
    if continuar == 'N':
        break
print('------FIM DO PROGRAMA------')
print(f'O total da compra foi de {soma:.2f} R$.')
print(f'Temos {maior1000} com mais de 1000 R$.')
print(f'O produto mais barato comprado foi o {produto_barato} e o valor dele é de {menor_valor:.2f}R$. ')
