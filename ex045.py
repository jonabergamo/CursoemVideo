from random import randint
from time import sleep
print('Suas opções: \n1 - Pedra\n2 - Papel\n3 - Tesoura\n')
jogada_player = int(input('Qual a sua jogada?: '))

if jogada_player < 1 or jogada_player > 3:
    print('\nEscolha uma opção válida!\n\n')
    exit()

jogadaIA = randint(1, 3)

player_escolha = 'Pedra' if jogada_player == 1 else 'Papel' if jogada_player == 2 else 'Tesoura'
IA_escolha = 'Pedra' if jogadaIA == 1 else 'Papel' if jogadaIA == 2 else 'Tesoura'

# | Pedra = 1 | Papel = 2 | Tesoura = 3 |
sleep(1)
print('-='*2)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!')
print('-='*2, '\n')

if jogada_player == 1 and jogadaIA == 3 or jogada_player == 2 and \
   jogadaIA == 1 or jogada_player == 3 and jogadaIA == 2:
    print('Você ganhou! {} vence {}'.format(player_escolha, IA_escolha))
elif player_escolha == IA_escolha:
    print('Empate! Ambos escolhemos {}!'.format(player_escolha, IA_escolha))
else:
    print('Eu ganhei! {} vence {}!'.format(player_escolha, IA_escolha))


