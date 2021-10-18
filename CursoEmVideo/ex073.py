# Crie uma tupla preenchida com os 20 primeiros colocados
# da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
#
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times_brasileirao = ('Atlético-MG', 'Flamengo', 'Fortaleza', 'Palmeiras',
                     'Bragantino', 'Corinthians', 'Internacional', 'Fluminense',
                     'Cuiabá', 'Athletico-PR', 'Atlético-GO', 'América-MG', 'Ceará SC',
                     'São Paulo', 'Santos', 'Bahia', 'Juventude', 'Sport Recife', 'Grêmio',
                     'Chapecoense')

print('5 primeiros colocados:')
for time in times_brasileirao[:5]:
    print(time)

print('\n4 últimos colocados:')
for time in times_brasileirao[-4:]:
    print(time)

print('\nTimes em ordem alfabética:')
for time in sorted(times_brasileirao):
    print(time)

print('\nPosição do Chapecoense?')
print(times_brasileirao.index('Chapecoense') + 1)