real = float(input('Quanto dinheiro vc tem? R$'))
dolar = real / 5.36
euro = real / 6.43
iene = real / 0.051
bitcoin = real / 0.0000052
print('Com R${:.2f} reais vc poderá comprar US${:.2f}'.format(real, dolar))
print('Com R${:.2f} reais vc poderá comprar {:.2f} euros'.format(real, euro))
print('Com R${:.2f} reais vc poderá comprar {:.2f} ienes'.format(real, iene))
print('Com R${:.2f} reais vc poderá comprar {:.2f} BTC'.format(real, bitcoin))




