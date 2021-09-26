print('*' * 47)
print('DIGITE 2 NÚMEROS ABAIXO PARA COMPARAR O MAIOR!')
print('*' * 47)
num1 = float(input('1º Número: '))
num2 = float(input('2º Número: '))
if num1 > num2:
    print('O 1º valor é MAIOR!')
elif num2 > num1:
    print('O 2º valor é MAIOR!')
else:
    print('Os 2 valores são EQUIVALENTES!')
