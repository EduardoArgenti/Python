# Crie um programa onde o usuário possa digitar vários valores
# numéricos e cadastre-os em uma lista. Caso o número já
# exista lá dentro, ele não será adicionado. No final,
# serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = list()

c= 0
while True:
    n = int(input(f'Valor {c+1}: '))
    if n not in valores:
        valores.append(n)
    op = input('Deseja digitar um novo valor?: ')
    if op in 'Nn':
        break
    c += 1

print(f'\nValores únicos digitados em ordem crescente: {sorted(valores)}')