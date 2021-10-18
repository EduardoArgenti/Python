# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma
# PA, mostrando os 10 primeiros termos da progressão usando a
# estrutura while.

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao

#for i in range(primeiro, decimo + razao, razao):
#    print(f'{i} ', end= '-> ')

c = primeiro
while c != decimo + razao:
    if c == decimo:
        print('{}'.format(c))
        break
    else:
        print('{} '.format(c), end='-> ')
    c += razao