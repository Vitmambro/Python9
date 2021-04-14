n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Seu primeiro nome seria {}'.format(nome[0]))
print('Seu ultimo nome seria {} '.format(nome[len(nome)-1]))

