# Crie um programa que gerencie o aproveitamento de um
# jogador de futebol. O programa vai ler o nome do jogador
# e quantas partidas ele jogou. Depois vai ler a quantidade
# de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário, incluindo o total de gols feitos
# durante o campeonato.
#
# A solução pensada foi um pouco diferente da proposta do exercício,
# mas também funciona.

jogador = list()
partidas = dict()

jogador.append(input('Nome do jogador: '))
total_partidas = int(input('Partidas jogadas: '))
jogador.append(total_partidas)

total_gols = 0
for c in range(0, total_partidas):
    gols = int(input(f'Gols feitos na partida {c}:' ))
    partidas[f'partida{c}'] = gols
    total_gols += gols

jogador.append(partidas)
jogador.append(total_gols)

print(f'\nNome: {jogador[0]}\nPartidas jogadas: {jogador[1]}\nGols: {jogador[2]}\nGols totais: {jogador[3]}')