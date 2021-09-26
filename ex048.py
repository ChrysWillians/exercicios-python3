soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A Soma de todos os {} valores dos números múltiplos de 3 de 1 a 500 são: {}'.format(cont, soma))
