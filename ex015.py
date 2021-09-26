km = float(input('Quantos km você andou? '))
dias = float(input('Quantos dias você utilozou o carro? '))
total = (km*0.15) + (dias*60)
print('O total a pagar é: R${:.2f}'.format(total))