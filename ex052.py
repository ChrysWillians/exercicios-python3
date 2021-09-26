n = int(input('Digite um número inteiro: '))
for c in range(1, n + 1):
    print('{} '.format(c), end=' ')
if n % 1 == 0 and n % n == 0:
    print('{} É um número primo'.format(n))
else:
    print('{} NÃO É UM NÚMERO PRIMO!'.format(n))

