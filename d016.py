'''import math
numero = float(input('Digite um número: '))
# print('O número {} tem a porção inteira {}.'.format(numero, (numero//1)))
# print('O número {} tem a porção inteira {:.0f}.'.format(numero, numero))
# print('O número {} tem a porção inteira {}.'.format(numero, math.modf(numero)))
print('O número {} tem a parte inteira {}'.format(numero, math.trunc(numero)))'''
#
num = float(input('Digite um número: '))
print('O número digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))