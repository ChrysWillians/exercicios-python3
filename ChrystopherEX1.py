

print('Digite o cumprimento de 3 retas para ver se ela forma um triângulo:')
reta1 = float(input('Reta 1: '))
reta2 = float(input('Reta 2: '))
reta3 = float(input('Reta 3: '))
if  reta1 > reta2 + reta3:
    print('As retas acima NÃO PODEM formar um Triângulo')
if reta2 > reta1 + reta3:
    print('As retas acima NÃO PODEM formar um Triângulo')
if reta3 > reta1 + reta2:
    print('As retas acima NÃO PODEM formar um Triângulo')
else:
    print('As retas acima PODEM formar um triângulo!')



