soma = 0
cont = 0
print('='*52)
print('''Digite seis números abaixo para efetuar a soma
Lembrando que só irá somar somente os números pares''')
print('='*52)
for c in range(1, 7):
    n = int(input('{}º número: '.format(c)))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print('A soma de todos os {} números PARES são: {}'.format(cont, soma))
