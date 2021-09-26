km = float(input('Quantos km do carro? '))
if km <= 80:
    print('Você está dentro do limite permitido, Continue assim e tenha um BOM DIA!')
else:
    print('MULTADO! Você ultrapassou o limite de velocidade permitido QUE É DE 80 KM/H!')
    multa = (km - 80) * 7
    print('O valor que você precisa pagar da multa é de {:.2f} R$'.format(multa))


