# ordem de precedencia

# 1 == ()
# 2 == **
# 3 == * , / , // , %
# 4 == + , -

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma e: {} o produto e: {} a divisao e: {:.3f}'.format(s, m, d), end='  ')
print('Divisao inteira: {} e potencia {}'.format(di, e))


