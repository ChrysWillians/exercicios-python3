from time import sleep
import random
escolha = ('Pedra', 'Papel', 'Tesoura')
pc = random.randint(0, 2)
print('Escolha uma opção abaixo para jogar JO KEN PO com o computador, Boa Sorte!')
print('''Opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual você escolhe?'))
print('...JO...')
sleep(1)
print('...KEN...')
sleep(1)
print('...PO!')
print('Você escolheu {}'.format(escolha[jogador]))
print('O computador escolheu {}'.format(escolha[pc]))
if pc == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('VOCÊ GANHOU, PARABÉNS!')
    elif jogador == 2:
        print('VOCÊ PERDEU, TENTE NOVAMENTE!')
    else:
        print('JOGADA INVÁLIDA!')
elif pc == 1:
    if jogador == 0:
        print('VOCÊ PERDEU, TENTE NOVAMENTE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('VOCÊ GANHOU, PARABÉNS!')
    else:
        print('JOGADA INVÁLIDA!')
elif pc == 2:
    if jogador == 0:
        print('VOCÊ GANHOU, PARABÉNS!')
    elif jogador == 1:
        print('VOCÊ PERDEU, TENTE NOVAMENTE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
