print('Digite 3 números abaixo:')
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))
if n1 > n2 and n1 > n3:
    print('O maior número é o {}'.format(n1))
if n2 > n1 and n2 > n3:
    print('O maior número é o {}'.format (n2))
if n3 > n1 and n3 > n1:
    print('O maior número é o {}'.format(n3))
if n1 < n2 and n1 < n3:
    print('E o menor número é o {}'.format(n1))
if n2 < n1 and n2 < n3:
    print('E o menor número é o {}'.format(n2))
if n3 < n1 and n3 < n2:
    print('E o menor número é o {}'.format(n3))



