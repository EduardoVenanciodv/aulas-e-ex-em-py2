aluno = str(input('Digite o nome do aluno:'))
n1 = float(input('Digite a primeira nota do aluno {}:'.format(aluno)))
n2 = float(input('Digite o segunda nota do aluno:'))

m = (n1 + n2) / 2

print('Com {:.1f} e {:.1f} a media dele é {:.1f}'.format(n1,n2,m))

if m < 5.0:
    print('REPROVADO!')
elif m > 4.9 and m < 7.0:
    print('Recuperação!')
else:
    print('PASSOU')
