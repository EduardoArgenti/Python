# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
jogadas = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
jogador = int(input('(1) Pedra\n(2) Papel\n(3) Tesoura\n')) - 1

print('\nComputador jogou {}'.format(jogadas[computador]))
print('Você jogou {}'.format(jogadas[jogador]))
if computador == 0: # Computador jogou Pedra
    if jogador == 0: # Pedra
        print('Empate!')
    elif jogador == 1:
        print('Você ganhou!')
    elif jogador == 2:
        print('Eu ganhei!')
elif computador == 1: # Computador jogou Papel
    if jogador == 0:
        print('Eu ganhei!')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Você ganhou!')
elif computador == 2: # Computador jogou Tesoura
    if jogador == 0:
        print('Você ganhou!')
    elif jogador == 1:
        print('Eu ganhei!')
    elif jogador == 2:
        print('Empate!')
