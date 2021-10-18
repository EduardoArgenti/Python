# Crie um programa que leia um número real qualquer pelo teclado e mostre
# na tela a sua porção inteira.
# Ex: digite um número 6.127, a sua parte inteira é 6.
from math import trunc

num = float(input('Número Real: '))

print(f'Parte inteira de {num} = {trunc(num)}')