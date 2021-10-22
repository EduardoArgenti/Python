# Faça um mini-sistema que utilize o interactive help
# do Python. O usuário vai digitar o comando e o manual
# vai aparecer. Quando o usuário digitar 'FIM', o programa
# se encerrará.
#
# OBS: use cores.

# Funções
def linhaTopo():
    print('\033[0:0:44m', end='')
    print('-=' * 25)
    texto = 'Sistema de Ajuda PyHelp'
    print(texto.center(50))
    print('-=' * 25)
    print('\033[0m', end='')


# Bloco principal
while True:
    linhaTopo()
    comando = input('Comando > ')
    if comando in 'FIMfim':
        break
    else:
        print(f'\033[0;30;45m{help(comando)}')

print('Finalizando o programa')
