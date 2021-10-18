# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até
# 200km e R$ 0,45 para viagens mais longas.

dist = float(input('Distância (km): '))

if dist > 200:
    preco_passagem = dist * 0.45
else:
    preco_passagem = dist * 0.50

print(f'Preço da passagem: R$ {preco_passagem}')