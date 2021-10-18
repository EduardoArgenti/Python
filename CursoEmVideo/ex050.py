# Desenvolva um programa que leia seis números inteiros e
# mostre a soma apenas daqueles que forem pares. Se o
# valor digitado for ímpar, desconsidere-o.

soma_pares = 0

for i in range(1,7):
    num = int(input(f'Valor {i}: '))
    if num % 2 == 0:
        soma_pares += num

print(f'\nA soma dos pares digitados é: {soma_pares}')