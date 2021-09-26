print('/' * 15)
print('CALCULE SEU IMC')
print('/' * 15)
altura = float(input('Digite sua altura  m: '))
peso = float(input('Digite seu peso:  KG '))
imc = peso / (altura ** 2)
print('seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está Abaixo do peso!')
elif imc <= 25:
    print('Você está com peso ideal!')
elif imc <= 30:
    print('Você está em Sobrepeso!')
elif imc <= 40:
    print('Você está com Obesidade!')
else:
    print('Você está com Obesidade Mórbida!')




