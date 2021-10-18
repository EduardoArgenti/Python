# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('N1: '))
b = int(input('N2: '))
c = int(input('N3: '))

# Verificando o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# Verificando o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'\nMenor valor: {menor}')
print(f'\nMaior valor: {maior}')
