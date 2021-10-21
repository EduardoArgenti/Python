# Crie um programa onde 4 jogadores joguem um dado e
# tenham resultados aleatórios. Guarde esses resultados
# em um dicionário em Python. No final, coloque esse
# dicionário em ordem, sabendo que o vencedor tirou o
# maior número no dado.

from random import randint
from operator import itemgetter
from time import sleep

jogadas = {'jogador1': randint(1, 6),
           'jogador2': randint(1, 6),
           'jogador3': randint(1, 6),
           'jogador4': randint(1, 6)}

conjunto = list()
conjunto = sorted(jogadas.items(), key=itemgetter(1), reverse=True)

for k, v in enumerate(conjunto):
    print(f'{k+1} lugar: {v[0]} com {v[1]}.')
    sleep(1)

