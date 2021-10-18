# Faça um programa que leia a largura e altura
# de uma parede em metros, calcule sua área
# e a quantidade de tinta necessária para
# pintá-la, sabendo que cada litro de tinta
# pinta uma área de 2m^2.

largura = float(input('Largura: '))
altura = float(input('Altura: '))
area = largura * altura
qtd_tinta = area / 2

print(f'Uma parede {largura} X {altura} precisará de {qtd_tinta} litros de tinta.')