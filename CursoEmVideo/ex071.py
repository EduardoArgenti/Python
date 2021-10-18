# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
#
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

notas_50 = notas_20 = notas_10 = notas_1 = resto = 0

while True:
    print('*****SAQUE*****')
    saque = int(input('Valor do saque: R$ '))

    if saque >= 50:
        notas_50 = saque // 50
        resto = saque % 50
    if resto >= 20:
        notas_20 = resto // 20
        resto = resto % 20
    if resto >= 10:
        notas_10 = resto // 10
        resto = resto % 10
    if resto >= 1:
        notas_1 = resto

    print('\n')
    print(f'Notas de 50: {notas_50}')
    print(f'Notas de 20: {notas_20}')
    print(f'Notas de 10: {notas_10}')
    print(f'Notas de 1: {notas_1}')
    op = input('\nDeseja realizar outro saque? (S/N): ')
    if op in 'Nn':
        break
    print('\n')