from math import sin, cos, tan, radians
angulo = float(input('Digite o ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('Para o ângulo de {:.2f} o valor do seno é {:.2f}, do cosseno é {:.2f} e a tangente é {:.2f}'.format(angulo, seno, cosseno, tangente))
