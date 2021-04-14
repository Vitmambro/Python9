dias = int(input('Dias alugados: '))
km = float(input('Quantos km rodados: '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar seria: {:.2f}'.format(pago))
