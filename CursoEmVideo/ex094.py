# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os
# dicionários em uma lista. No final, mostre:
#
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoa = dict()
conj_pessoas = list()

i = 0
while True:
    print(f'Pessoa {i+1}: ')
    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = input('Sexo: ')
    pessoa['idade'] = int(input('Idade: '))

    conj_pessoas.append(pessoa.copy())

    pessoa.clear()

    op = input('Deseja adicionar mais uma pessoa? (S / N): ')
    if op in 'Nn':
        break

    i += 1

print(f'\nPessoas cadastradas: {len(conj_pessoas)}')

lista_mulheres = list()
soma_idades = 0
for c in range(0, len(conj_pessoas)):
    soma_idades += conj_pessoas[c]['idade']
    if conj_pessoas[c]['sexo'] in 'Ff':
        lista_mulheres.append(conj_pessoas[c].copy())

media = soma_idades/len(conj_pessoas)

print(f'Média de idades: {media}')

print('Mulheres: ', end='')
for c in range(0, len(lista_mulheres)):
    print(f'{lista_mulheres[c]["nome"]}', end='...')

lista_idades_acima_media = list()
for c in range(0, len(conj_pessoas)):
    if conj_pessoas[c]['idade'] > media:
        lista_idades_acima_media.append(conj_pessoas[c].copy())
print('\nPessoas com idade acima da média: ', end='')
for c in range(0, len(lista_idades_acima_media)):
    print(f'{lista_idades_acima_media[c]["nome"]}', end='...')
