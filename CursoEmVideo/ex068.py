# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele
# conquistou no final do jogo.

from random import randint

vitorias_player = 0

while True:
    modo = int(input('(1) Ímpar ou (2) Par?: '))
    jogada_pc = randint(1, 5)
    jogada_player = int(input('Qual sua jogada?: '))
    total = jogada_pc + jogada_player

    print(f'\nJogador: {jogada_player}\nComputador: {jogada_pc}')
    print(f'Soma: {total}')

    if total % 2 == 0 and modo == 2: # Soma deu par e jogador escolheu par
        print(f'Você ganhou!')
        vitorias_player += 1
    elif total % 2 == 0 and modo == 1: # Soma deu par e jogador escolheu ímpar
        print(f'\nVocê perdeu!')
        break
    elif total % 2 == 1 and modo == 1: # Soma deu ímpar e jogador escolheu ímpar
        print(f'Você ganhou!')
        vitorias_player += 1
    elif total % 2 == 1 and modo == 2: # Soma deu ímpar e jogador escolheu par
        print('\nVocê perdeu!')
        break
    print('\n')

print(f'{vitorias_player} vitórias consecutivas')