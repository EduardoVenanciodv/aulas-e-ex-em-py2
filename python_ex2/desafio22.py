s = ''
while s != 'M' and s != 'F':
    s = str(input('Digite seu sexo (M/F):')).upper()
if s == 'F':
    print('Seu sexo é Feminino.')
else:
    print('Seu sexo é Masculino.')



