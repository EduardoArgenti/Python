# Crie um programa que vai gerar cinco números aleatórios
# e colocar em uma tupla. Depois disso, mostre a listagem
# de números gerados e também indique o menor e o maior
# valor que estão na tupla.

from random import randint

aleatorios = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))

print(f'Números gerados: {aleatorios}')

menor = maior = aleatorios[0]
for pos, num in enumerate(aleatorios):
    if aleatorios[pos] < menor:
        menor = aleatorios[pos]
    if aleatorios[pos] > maior:
        maior = aleatorios[pos]

print(f'Menor valor: {menor}\nMaior valor: {maior}')

