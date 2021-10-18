# Crie um programa que leia o nome de uma cidade e diga se ela começa
# ou não com o nome "SANTO".

cidade = input('Nome da cidade: ')

print(f'A cidade "{cidade.strip()}" possui "Santo" no nome?', 'santo' in cidade.lower().strip())