# Crie um programa onde o usuário possa digitar sete valores
# numéricos e cadastre-os em uma lista única que mantenha
# separados os valores pares e ímpares. No final, mostre os
# valores pares e ímpares em ordem crescente.

pares = list()
impares = list()
valores = list()
# Estabeleço uma conexão entre pares e valores[0] e ímpares e valores[1]
# propositalmente para atualizar a lista geral quando mudar os pares ou ímpares.
valores.append(pares)
valores.append(impares)

for c in range(0, 7):
    n = int(input(f'Valor {c+1}: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

valores[0].sort()
valores[1].sort()
print(f'\nElementos pares: {valores[0]}')
print(f'Elementos ímpares: {valores[1]}')

