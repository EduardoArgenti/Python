# Faça um programa que ajude um jogador da MEGA SENA a criar
# palpites. O programa vai perguntar quantos jogos serão gerados
# e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

conj_jogos = list()

n = int(input('Quantos jogos serão gerados?: '))

c = 0
for c in range(0, n):
    jogo = list()
    count_num = 0
    while True:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            count_num += 1
        if count_num == 6:
            break
    jogo.sort()
    conj_jogos.append(jogo[:])
    jogo.clear()

for pos, j in enumerate(conj_jogos):
    print(f'Jogo {pos+1}: {j}')
    sleep(1)



