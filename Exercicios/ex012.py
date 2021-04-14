p = float(input('Valor do produto: '))
prazo = p + (p * 10 / 100)
vista = p - (p * 5 / 100)
print('O produto custa {:.2f}, pagando a prazo ficará {:.2f} e pagando a vista ficará {:.2f}'.format(p, prazo, vista))
