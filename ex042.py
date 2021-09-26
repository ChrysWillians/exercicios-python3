print('/' * 25)
print('Digite 3 segmentos para ver se elas podem formar um triângulo, e o tipo de triângulo:')
print('/' * 25)
seg1 = float(input('Digite o 1º segmento: '))
seg2 = float(input('Digite o 2º segmento: '))
seg3 = float(input('Digite o 3º segmento: '))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Os segmentos PODEM FORMAR o Triângulo ', end=' ')
    if seg1 == seg2 == seg3:
        print('EQUILÁTERO!')
    elif seg1 != seg2 != seg3 != seg1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos NÃO PODEM formar nenhum tipo de triângulo!')


