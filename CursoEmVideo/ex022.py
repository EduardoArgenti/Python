# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas
# - O nome com todas minúsculas
# - Quantas letras ao todo (sem considerar espaços)
# - Quantas letras tem o primeiro nome

nome = input('Nome: ')
print('Caixa alta: ', nome.upper())
print('Caixa baixa: ', nome.lower())
print('Qtd de letras: ', len(nome) - nome.count(' '))

nome_dividido = nome.split()
print(f'Primeiro nome: {len(nome_dividido[0])} letras')


