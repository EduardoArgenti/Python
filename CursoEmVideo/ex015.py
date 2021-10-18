# Escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi
# alugado. Calcule o preço a pagar, sabendo que o carro custa R$60
# por dia e R$0,15 por Km rodado.

km = float(input('Km percorridos: '))
dias = int(input('Dias: '))

preco = (km * 0.15) + (dias * 60)

print('\nPreço a pagar: R$ {:.2f}'.format(preco))