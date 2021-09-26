#num = int(input('Digite um número de 0 a 9999:'))
#n = num(str)
#print('unidade {}'.format(n[3]))
#print('dezena {}'.format(n[2]))
#print('centena {}'.format(n[1]))
#print('milhar {}'.format(n[0]))

num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(u, d, c, m))
