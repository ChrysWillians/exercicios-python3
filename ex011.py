larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg * alt
print('Sua parde tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, area, area ** (1/2)))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}L de tinta'.format(tinta))
