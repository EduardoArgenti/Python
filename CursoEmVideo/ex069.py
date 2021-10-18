# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o
# usuário quer ou não continuar. No final, mostre:
#
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

count = 1
pessoas_mais_18_anos = tot_homens = mulheres_menos_20_anos = 0

while True:
    print(f'Pessoa {count}')
    idade = int(input('Idade: '))
    sexo = input('Sexo: ')

    if idade >= 18:
        pessoas_mais_18_anos += 1
    if sexo in 'Mm':
        tot_homens += 1
    if sexo in 'Ff' and idade < 20:
        mulheres_menos_20_anos += 1

    op = input('Deseja cadastrar mais alguém? (S/N): ')

    if op in 'Nn':
        break
    count += 1

print(f'{pessoas_mais_18_anos} pessoas são maiores de 18.')
print(f'{tot_homens} pessoas são homens.')
print(f'{mulheres_menos_20_anos} pessoas são mulheres com menos de 20 anos.')
