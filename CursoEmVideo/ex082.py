# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os
# valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

valores = list()
pares = list()
impares = list()

i = 0

while True:
    n = int(input(f'Valor {i+1}: '))
    valores.append(n)

    op = input('Continuar? (S/N): ')
    if op in 'Nn':
        break
    i += 1

for c in valores:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)

print('\n')
print(f'Lista original: {valores}')
print(f'Pares: {pares}')
print(f'Ímpares: {impares}')