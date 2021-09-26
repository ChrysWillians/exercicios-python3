preço = float(input('Digite o preço do produto: '))
desconto = float(input('Digite o desconto oferecido: '))
novo = preço - (preço * desconto / 100)
print('O produto que custava R${:.2f}, vai passar a custar R${:.2f} com {:.2f}% de desconto'.format(preço, novo, desconto))
