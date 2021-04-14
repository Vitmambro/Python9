salario = float(input('Salario do funcionario: '))
aum = salario + (salario * 15 / 100)
print('O salario era R${:.2f}, com aumento de 15% ficaria R${:.2f}'.format(salario, aum))
