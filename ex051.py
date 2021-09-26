print('=' * 30)
print('10 PRIMEIROS TERMOS DE UMA PA')
print('=' * 30)
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = t + (10 - 1) * r
for c in range(t, d + r, r):
    print('{}'.format(c), end=' >')
print('ACABOU!')
