# Crie um programa que leia o ano de nascimento de
# sete pessoas. No final, mostre quantas pessoas
# ainda não atingiram a maioridade e quantas já são maiores.

from datetime import datetime

jovens = 0
adultos = 0
ano_atual = datetime.now().year


for i in range(1,8):
    ano_nasc = int(input(f'Ano de nascimento {i}: '))
    idade = ano_atual - ano_nasc
    if idade < 18:
        jovens += 1
    else:
        adultos += 1

print(f'\nMenores de idade: {jovens} pessoas')
print(f'Maiores de idade: {adultos} pessoas')
