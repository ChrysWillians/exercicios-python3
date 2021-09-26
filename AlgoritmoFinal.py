import geopy.distance

latitudepet = float(input('Digite a Latitude do seu PET: '))
longitudepet = float(input('Digite a Longitude do seu PET: '))
latitudedono = float(input('Digite a sua Latitude: '))
longitudedono = float(input('Digite sua Longitude: '))

p1 = (latitudepet, longitudepet)
p2 = (latitudedono, longitudedono)
diferenca = (geopy.distance.distance(p1, p2).km)

if diferenca > 0.02:
    print('\033[1;31mALERTA: SEU PET SAIU DA ÁREA DE SEGURANÇA!')
else:
    print('Seu pet está dentro da área de segurança.')