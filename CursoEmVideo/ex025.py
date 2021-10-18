# Crie um programa que leia o nome de uma pessoa e diga se ela tem
# "SILVA" no nome

nome = input('Nome: ')

print(f'"{nome}" possui "Silva"?', 'silva' in nome.lower())