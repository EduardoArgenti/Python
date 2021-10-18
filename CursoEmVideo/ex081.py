# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
#
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

valores = list()
tot_num = i = 0

while True:
    n = int(input(f'Valor {i+1}: '))
    valores.append(n)
    tot_num += 1
    op = input('Continuar? (S/N): ')
    if op in 'Nn':
        break
    i += 1

print('\n')
print(f'Lista: {valores}')
print(f'Números digitados: {tot_num}')
valores.sort(reverse=True)
print(f'Lista em ordem decrescente: {valores}')
if 5 in valores:
    print('O valor 5 foi digitado!')
else:
    print('O valor 5 NÃO foi digitado!')