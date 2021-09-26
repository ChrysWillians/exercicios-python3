# from math import hypot
# cateto1 = float(input('Digite o cumprimento do cateto oposto: '))
# cateto2 = float(input('Digite o cumprimento do cateto adjacente: '))
# h = hypot(cateto1, cateto2)
# print('A hipotenusa dos catetos é igual a {:.2f}'.format(h))


print ('=' * 40)
cateto1 = float(input('Digite o cumprimento do cateto oposto: '))
cateto2 = float(input('Digite o cumprimento do cateto adjacente: '))
h = (cateto1 **2 + cateto2 ** 2) **(1/2)
print('A hipotenusa dos catetos é igual a {:.2f}'.format(h))
print('=' * 40)




