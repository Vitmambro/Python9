distancia = float(input('Qual a distancia da sua viagem? '))
print('Voce fara uma viagem de {:.2f}km'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('Sua passagem custara R${:.2f}'.format(preço))

