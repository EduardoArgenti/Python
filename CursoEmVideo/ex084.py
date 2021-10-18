# Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
#
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

dado = list()
pessoas = list()

i = menor_peso = maior_peso = 0
while True:
    print(f'Pessoa {i+1}')
    dado.append(input('Nome: '))
    dado.append(float(input('Peso: ')))

    if len(pessoas) == 0:
        menor_peso = maior_peso = dado[1]
    else:
        if dado[1] > maior_peso:
            maior_peso = dado[1]
        if dado[1] < menor_peso:
            menor_peso = dado[1]

    pessoas.append(dado[:])
    dado.clear()

    op = input('Continuar? (S/N): ')
    if op in 'Nn':
        break
    i += 1

print(f'\nPessoas cadastradas: {len(pessoas)}')
print(f'O maior peso foi {maior_peso} kg das pessoas:', end=' ')
for p in pessoas:
    if p[1] == maior_peso:
        print(f'{p[0]}', end='... ')

print(f'\nO menor peso foi {menor_peso} kg das pessoas:', end=' ')
for p in pessoas:
    if p[1] == menor_peso:
        print(f'{p[0]}', end='... ')





