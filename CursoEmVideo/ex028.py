# Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 a 5 e peça para o usuário tentar descobrir qual foi o número
# escolhido pelo computador. O programa deverá escrever na tela se o
# usuário venceu ou perdeu.

from random import randint

aleatorio = randint(0,5)

chute = int(input('Qual número o computador pensou? '))

if chute == aleatorio:
    print('Você acertou!')
else:
    print(f'Você errou! O número pensado foi {aleatorio}')