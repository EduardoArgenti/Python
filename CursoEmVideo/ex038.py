# Escreva um programa que leia dois números inteiros e compare-os
# mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))

if a > b:
    print(f'\n{a} é maior que {b}!')
elif a < b:
    print(f'\n{b} é maior que {a}!')
else:
    print('\nNão existe valor maior! Ambos são iguais.')