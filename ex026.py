frase = str(input('Digite uma frase: ')).lower().strip()
aqt = frase.count('a')
a1 = frase.find('a')+1
au = frase.rfind('a')+1
print('A frase tem {} letras "a"'.format(aqt))
print('A letra "a" aparece pela 1º vez na posição {}'.format(a1))
print('A última letra "a" aparece na posição {}'.format(au))

