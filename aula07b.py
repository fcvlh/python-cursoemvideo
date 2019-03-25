n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
# print('A soma entre {} e {} é {}'.format(n1, n2, n1+n2))
a = n1 + n2
s = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
r = n1 % n2
print('Soma {}\nsubtração {}\nmultiplicação {}\ndivisão {}'.format(a, s, m, d))
print('Divisão inteiro {}\nexponenciação {}\nresto {}'.format(di, e, r))
