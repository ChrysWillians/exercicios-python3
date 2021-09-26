from datetime import date
ano = date.today().year
nascimento = int(input('Digite o ano em que você nasceu: '))
categoria = ano - nascimento

if categoria <= 9:
    print('Com {} anos, você é da categoria MIRIM!'.format(categoria))
elif categoria <= 14:
    print('Com {} anos, você é da categoria INFANTIL!'.format(categoria))
elif categoria <= 19:
    print('Com {} anos, você é da categoria JUNIOR!'.format(categoria))
elif categoria <= 25:
    print('Com {} anos, você é da categoria SÊNIOR!'.format(categoria))
elif categoria > 25:
    print('com {} anos, você é da categoria MASTER!'.format(categoria))

