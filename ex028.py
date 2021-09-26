from random import randint
from time import sleep
computador = randint(0,5)
print('#-'*30)
print('Vou pensar em um número entre 0 e 5 tente adivinhar.....')
print('#-'*30)
player = int(input('Em que número eu pensei? '))
print('PROCESSANDO....')
sleep(4)
if player == computador:
    print('Você acertou, PARABÉNS!')
else:
    print('Você errou, tente novamente.')
print('o número que eu pensei foi o {}'.format(computador))



