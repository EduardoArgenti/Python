# Melhore o DESAFIO 61, perguntando para o usuário se ele
# quer mostrar mais alguns termos. O programa encerrará
# quando ele disser que quer mostrar 0 termos.

op = 1

while op != 0:
    primeiro = int(input('Primeiro termo: '))
    razao = int(input('Razão: '))
    decimo = primeiro + (10 - 1) * razao

    c = primeiro
    while c != decimo + razao:
        if c == decimo:
            print('{}'.format(c))
            break
        else:
            print('{} '.format(c), end='-> ')
        c += razao
    op = int(input('\nDeseja mostrar mais termos? (1 SIM / 0 NAO)'))