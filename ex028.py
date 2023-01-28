from random import randint
from time import sleep
palpite = int(input('hmm, Estou pensando em um número inteiro entre 0 e 5, qual é?: '))
numero = random.randint(0, 5)  # sorteia os números
if 5 >= palpite >= 0:
    if palpite == numero:
        print('Você acertou! Eu estava mesmo pensando no número {}!'.format(numero))
    else:
        print('Você errou! Eu estava pensando no número {}!'.format(numero))
else:
    print('{} está fora da escala!'.format(palpite))
