import math
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
hi = math.hypot(ca, co)
print('A hipotenusa vai medir {:.2f}'.format(hi))


''' hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi)) '''
