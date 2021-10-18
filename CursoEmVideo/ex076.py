# Crie um programa que tenha uma tupla única com nomes
# de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando
# os dados em forma tabular.

precos = ('Creme dental', 7.99,
          'Analgésico', 29.99,
          'Vitamina C', 15.50,
          'Aspirina', 19.99,
          'Termômetro', 49.99,
          'Barra de cereal', 4.99,
          'Barbeador', 6.99)

print('Produtos: ')
pos = 0
while pos < len(precos):
    print(f'{precos[pos]:.<25}R$ {precos[pos+1]:>5.2f}')
    pos += 2
