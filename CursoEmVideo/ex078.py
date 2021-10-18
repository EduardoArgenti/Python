# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as
# respectivas posições na lista (não basta pegar somente a primeira ocorrência!)

valores = list()

# O primeiro valor é inserido fora do loop para as definições do menor e maior valores!
maior = menor = int(input('Valor 1: '))
valores.append(maior)
i = 1

while i < 5:
    n = int(input(f'Valor {i+1}: '))
    valores.append(n)
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    i += 1

print(f'\nElementos da lista: {valores}')

print(f'Menor valor é {menor} encontrado nas posições:', end=' ')
i = 0
while i < len(valores):
    if valores[i] == menor:
        print(f'{i+1}', end=' ')
    i += 1

print(f'\nMaior valor é {maior} encontrado nas posições:', end=' ')
i = 0
while i < len(valores):
    if valores[i] == maior:
        print(f'{i+1}', end=' ')
    i += 1


