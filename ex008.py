n = float(input('Digite um valor para ser convertido: '))
km = n / 1000
cm = n * 100
mm = n * 1000
print('{}m corresponde a: \nkm = {}\ncm = {:.0f}\nmm = {:.0f}'.format(n, km, cm, mm))
