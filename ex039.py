from datetime import date
data = date.today().year
print('*' * 20)
print('ALISTAMENTO MILITAR')
print('*' * 20)
ano = int(input('Em que ano você nasceu: '))
idade = data - ano
alistamento = idade - 17
print('Quem nasce em {} tem {} anos de idade'.format(ano, idade))
if idade > 18:
    print('Você já passou do tempo de se alistar\nVocê já deveria ter feito o alistamento em {}!'.format(data - alistamento))
elif idade == 18:
    print('Você tem que ir se alistar IMEDIATAMENTE')
else:
    print('Você não tem idade mínima para o alistamento.\nVocê precisará se alistar em {} anos'.format(18 - idade))



