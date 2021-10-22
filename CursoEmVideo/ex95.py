# Aprimore o desafio 93 para que ele funcione com vários
# jogadores, incluindo um sistema de visualização de detalhes
# do aproveitamento de cada jogador.
#
# Lógica: listas para jogadores, que contém dicionários, que por sua vez contêm
# listas para os gols.

jogador = dict()
jogadores = list()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = input('Nome: ')
    total_partidas = int(input('Partidas jogadas: '))
    partidas.clear()
    for c in range(0, total_partidas):
        partidas.append(int(input(f'Gols na partida {c}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)

    jogadores.append(jogador.copy())

    op = input('\nQuer continuar? (S / N): ')
    if op in 'Nn':
        break

# Printar cabeçalho
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

# Printar dados de todos os jogadores
for k, v in enumerate(jogadores):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()

# Printar dados do jogador escolhido
while True:
    busca = int(input('Escolha o jogador: '))
    if busca == 999:
        break
    elif busca >= len(jogadores):
        print(f'Erro! Não existe jogador com código {busca}')
    else:
        print(f'Jogador {jogadores[busca]["nome"]}')
        for i, g in enumerate(jogadores[busca]['gols']):
            print(f'No jogo {i}, fez {g} gols.')
    print()

print('Finalização do programa!')



