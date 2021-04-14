medida = float(input('Distancia em metros: '))
cm = medida * 100
mm = medida * 1000
km = medida / 1000
print('A distancia de {:.1f} em cm seria {:.1f}, em mm seria {:.1f}, em km seria {:.1f}'.format(medida, cm, mm, km))
