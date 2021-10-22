# Faça um programa que tenha uma função chamada area( ), que receba
# as dimensões de um terreno retangular (largura e comprimento) e
# mostre a área do terreno.

# Função
def area(largura, comprimento):
    print(f'Área do terreno de {largura}x{comprimento}: {largura * comprimento}m^2')


# Bloco principal
largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))
area(largura, comprimento)

