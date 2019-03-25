km = float(input('Quantos quilometros rodados: '))
dias = int(input('Quantos dias alugado: '))
valordia = 60.0
valorkm = 0.15
total = (km * valorkm) + (dias * valordia)
print('O valor total a ser pago é de R$ {:.2f}.'.format(total))

