# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:
#
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

count = 1
tot_compra = preco_acima_mil = 0
menor_preco = 9999
prod_menor_preco = ''

while True:
    print(f'Produto {count}')
    nome_prod = input('Nome: ')
    preco_prod = float(input('Preço: '))

    tot_compra += preco_prod

    if preco_prod > 1000:
        preco_acima_mil += 1
    if preco_prod < menor_preco:
        menor_preco = preco_prod
        prod_menor_preco = nome_prod

    op = input('Deseja inserir mais algum produto? (S/N): ')
    if op in 'Nn':
        break
    count += 1

print('\nCompra finalizada!')
print(f'Total da compra: R$ {tot_compra}')
print(f'{preco_acima_mil} produtos custam mais de R$ 1.000,00')
print(f'O produto mais barato é {prod_menor_preco}')

