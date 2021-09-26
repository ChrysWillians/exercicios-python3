num = int(input('Digite um número inteiro para a conversão: '))
print(''''[1] Converter para Binário
[2] Converter para Octal
[3] Converter para Hexadecimal''')
conv = int(input('Qual a sua opção: '))
if conv == 1:
    print('{} convertido para Binário é igual a {}'.format(num, bin(num)[2:]))
elif conv == 2:
    print('{} convertido para Octal é igual a {}'.format(num, oct(num)[2:]))
elif conv == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('VOCÊ ESCOLHER UM NÚMERO QUE NÃO CORRESPONDE A NENHUMA DAS 3 OPÇÕES!')
