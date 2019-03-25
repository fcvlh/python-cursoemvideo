'''co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = (co ** 2 + ca ** 2) ** (1 / 2)
print('A hipotenusa para o cateto oposto {:.2f} e cateto adjacente {:.2f} é de {:.2f}'.format(co, ca, h))'''
#
from math import hypot
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
print('A hipotenusa para o cateto oposto {:.2f} e cateto adjacente {:.2f} é de {:.2f}'.format(co, ca, hypot(co, ca)))
