import math
an = float(input('Digite um angulo: '))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('O SENO do angulo {:.2f} eh igual a {:.2f}'.format(an, sen))
print('O COSSENO do angulo {:.2f} eh igual a {:.2f}'.format(an, cos))
print('A TANGENTE do angulo {:.2f} eh igual a {:.2f}'.format(an, tan))
