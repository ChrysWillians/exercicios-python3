casa = float(input('Qual o valor da casa financiada: R$'))
salario = float(input('Qual é o valor da sua renda mensal: R$'))
ano = int(input('Em quantos anos pretende parcelar a casa? '))
parcela = casa / (ano * 12)
pode = salario * 30 / 100
print('=' * 80)
if parcela >= pode:
    print('Emprestimo NEGADO! O valor da parcela ( R${:.2f} ) é maior que 30% do seu salário, Lamento!'.format(parcela))
else:
    print('Emprestimo APROVADO! Sua parcela ficará R${:.2f} por mês pagando em {} anos.'.format(parcela, ano))
print('=' * 80)