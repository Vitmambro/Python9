velocidade = float(input('Qual a velociade do carro?'))
if velocidade >80:
    print('MULTADO! Voce passou o limite de 80km')
    multa = (velocidade - 80) * 7
    print('Voce tera que pagar R${}'.format(multa))
else:
    print('Tenha um bom dia. Dirija com cuidado!')
