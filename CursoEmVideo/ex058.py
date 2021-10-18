# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar”
# em um número entre 0 e 10. Só que agora o jogador vai tentar
# adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.

from random import randint

aleatorio = randint(0,10)

chute = int(input('Qual número o programa pensou?: '))
soma_chutes = 1
while chute != aleatorio:
    chute = int(input('Tente novamente! Qual número o programa pensou?: '))
    soma_chutes += 1

print('Correto, o program pensou no número {}! Levou {} tentativas'.format(aleatorio, soma_chutes))
