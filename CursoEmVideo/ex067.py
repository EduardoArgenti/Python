# Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:
    n = int(input('Calcular a tabuada de: '))
    if n < 0:
        break
    count = 1
    while count < 11:
        print(f'{n} X {count} = {n*count}')
        count += 1

print('Programa finalizado!')