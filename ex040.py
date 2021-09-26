print('/' * 30)
print('Calcule a média de suas notas:')
print('/' * 30)
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
print('/' * 30)
media = (n1 + n2) / 2
print('A média de {:.1f} e {:.1f} foi: {:.1f}'.format(n1, n2, media))
print('/' * 30)
if media >= 7:
    print('PARABÉNS, você foi APROVADO!')
elif media < 5:
    print('Você foi REPROVADO!')
else:
    print('Você ficou de RECUPERAÇÃO!')
print('/' * 30)



