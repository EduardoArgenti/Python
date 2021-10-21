# Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

nome = input('Nome: ')
media = float(input('Média: '))

if media < 4:
    situacao = 'Reprovado'
elif 4 <= media <= 6:
    situacao = 'Recuperação'
elif 6 < media < 10:
    situacao = 'Aprovado'
else:
    situacao = 'Aprovado com excelência'

alunos = dict()

alunos['nome'] = nome
alunos['media'] = media
alunos['situacao'] = situacao

for k, v in alunos.items():
    print(f'{k}: {v}')

