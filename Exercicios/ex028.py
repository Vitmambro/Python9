from random import randint
from time import sleep
computador = randint(0, 5)
print('====' * 10)
print('Vou pensar em um numero de 0 a 5. Tente adivinhar...')
print('====' * 10)
jogador = int(input('Em que numero eu pensei?'))
print('PROCESSANDO....')
sleep(2)
if jogador == computador:
    print('Voce acertou !')
else:
    print('GANHEI ! Pensei no numero {} e nao no {}'.format(computador, jogador))

