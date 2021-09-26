salario = float(input('Digite o valor do seu salário para calcular seu aumento: R$ '))
aumento1 = salario * 15 / 100
if salario <= 1250:
    print('Seu salário agora é de R${:.2f}'.format(salario + aumento1))
aumento2 = salario * 10 / 100
if salario > 1250:
    print('Seu salário agora é de R${:.2f}'.format(salario + aumento2))
