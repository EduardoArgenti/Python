# Desenvolva um programa que leia o nome, idade e
# sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem
# mais velho e quantas mulheres têm menos de 20 anos.

soma_idades = 0
media_idades = 0
maior_idade_homem = 0
nome_homem_velho = ''
total_mulheres_20 = 0

for i in range (1, 5):
    print(f'Pessoa {i}: ')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).strip()
    soma_idades += idade

    if i == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_homem_velho = nome
    if idade > maior_idade_homem and sexo in 'Mm':
        maior_idade_homem = idade
        nome_homem_velho = nome
    if idade < 20 and sexo in 'Ff':
        total_mulheres_20 += 1

media_idades = soma_idades / 4
print('\nMédia de idade: {}'.format(media_idades))
print('Homem mais velho: {} com {} anos'.format(nome_homem_velho, maior_idade_homem))
print('{} mulheres têm idade menor do que 20 anos'.format(total_mulheres_20))

