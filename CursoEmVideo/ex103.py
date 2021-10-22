# Faça um programa que tenha uma função chamada ficha(), que receba
# dois parâmetros opcionais: o nome de um jogador e quantos gols ele fez.
#
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que
# algum dado não tenha sido informado corretamente.
#
# <desconhecido> e 0 gol(s) caso não for informado nenhum dos parâmetros.

# Função
def ficha(nome='<desconhecido>', gols=0):
    saida = f'O jogador {nome} fez {gols} gol(s).'

    return(saida)


# Bloco principal
print(ficha())