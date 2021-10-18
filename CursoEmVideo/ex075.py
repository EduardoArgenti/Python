# Desenvolva um programa que leia quatro valores pelo
# teclado e guarde-os em uma tupla. No final, mostre:
#
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

valores = (int(input('Valor 1: ')),
           int(input('Valor 2: ')),
           int(input('Valor 3: ')),
           int(input('Valor 4: ')))

print(f'\nValores digitados: {valores}')
print(f'9 apareceu {valores.count(9)} vezes.')
if 3 in valores:
    print(f'3 apareceu na posição {valores.index(3)+1} pela primeira vez.')
else:
    print('O valor 3 não aparece na lista.')
print('Valores pares: ', end=' ')
for c in valores:
    if c % 2 == 0:
        print(f'{c}', end=' ')
