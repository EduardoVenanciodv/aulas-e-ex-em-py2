al = float(input('Digite o tamanho da sua altura em metros: '))
kg = float(input('Digite seu peso corporal em kg: '))

imc = kg / (al * al)

if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('Peso ideal')
elif imc > 25 and imc <= 30:
    print('Sobrepeso')
elif imc > 30 and imc <= 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade Mórbida')

print('O IMC é de: {:.1f}'.format(imc))
