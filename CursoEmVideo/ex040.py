# Crie um programa que leia duas notas de um aluno e calcule
# sua média, mostrando uma mensagem no final, de acordo com
# a média atingida.
# - Média abaixo de 5.0: reprovado
# - Média entre 5.0 e 6.9: recuperação
# - Média 7.0 ou superior: aprovado

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))

media = (n1 + n2) / 2

print(f'\nMédia: {media}')
if media < 5:
    print('\nReprovado!')
elif 5 <= media <= 6.9:
    print('\nRecuperação!')
else:
    print('\nAprovado!')