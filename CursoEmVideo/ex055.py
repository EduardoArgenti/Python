# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

menor_peso = 999
maior_peso = -1

for i in range(1, 6):
    peso = float(input(f'Peso {i}: '))
    if peso > maior_peso:
        maior_peso = peso
    elif peso < menor_peso:
        menor_peso = peso

print(f'Menor peso: {menor_peso}')
print(f'Maior peso: {maior_peso}')
