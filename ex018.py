from math import cos, sin, tan, radians
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ângulo))
cosseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))
print('O seno de {} é {:.2f}'.format(ângulo, seno))
print('O cosseno de {} é {:.2f}'.format(ângulo, cosseno))
print('A tangente de {} é {:.2f}'.format(ângulo, tangente)
    )