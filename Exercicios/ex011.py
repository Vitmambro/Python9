larg = float(input('Largura da parede:' ))
alt = float(input('Altura da parede: '))
area = larg * alt
tinta = area / 2
print('Sua parede tem as dimensoes {}x{} e sua area é de {}m²'.format(larg, alt, area))
print('Para pintar a parede voce ira precisar de {:.2f}l de tinta'.format(tinta))

