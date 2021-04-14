nome = (input('Digite seu nome completo: ')).strip()
print('Nome em maiusculo: {}'.format(nome.upper()))
print('Nome em minusculo {}'.format(nome.lower()))
print('Quantidade de letras: {}'.format(len(nome) - nome.count(' ')))
#print('Letras no primeiro nome: {}'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome e´ {} e ele tem {} letras'.format(separa[0], len(separa[0])))







