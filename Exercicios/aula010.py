n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
m = (n1 + n2 + n3) / 3
print('Sua media foi {:.1f} '.format(m))
print('Aprovado' if m >= 6 else 'Reprovado')

# if m <= 6:
# print('Voce foi reprovado')
# else:
# print('Voce foi aprovado')
