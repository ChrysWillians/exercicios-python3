print('=' * 10,'LOJA - WILLIANS JC','=' * 10)
preço = float(input('Qual o valor do produto: '))
print('DIGITE UM DOS NÚMEROS ABAIXO PARA ESCOLHER UMA FORMA DE PAGAMENTOPARA E CONTINUAR A COMPRA!')
print('''[1] À Vista - 10% de DESCONTO. (Dinheiro ou Cheque)
[2] À Vista no Cartão - 5% de DESCONTO (Débito)'))
[3] 2x no Cartão de Crédito SEM JUROS'))
[4] 3x ou mais no Cartão - 20% de JUROS ADICIONAL''')
opcao = int(input('Digite a forma de pagamento que você prefere: '))
if opcao == 1:
    print('Você escolheu o pagamento à vista, o valor da sua compra ficará em R${:.2f}'.format(preço - (preço * 10 / 100)))
elif opcao == 2:
    print('Você escolheu o pagamento à vista no cartão, o valor da sua compra ficará em R${:.2f}'.format(preço - (preço * 5 / 100)))
elif opcao == 3:
    print('Você escolheu o pagamento no cartão de crédito em 2x sem juros, o valor da sua compra ficará em R${:.2f}, e cada parcela ficará em R${:.2f}.'.format(preço, preço / 2))
elif opcao == 4:
    total = preço + ((preço * 20) / 100)
    qntparc = int(input('Em quantas vezes você quer parcelar: '))
    parcelas = total / qntparc
    print('Você escolher o pagamento no cartão em {}x, o valor da sua compra ficará em R${:.2f}, e cada parcela ficará em R${:.2f}'.format(qntparc, total, parcelas))
else:
    print('/' * 42)
    print('ERRO! Você não digitou umas das 4 opções!')
    print('/' * 42)
