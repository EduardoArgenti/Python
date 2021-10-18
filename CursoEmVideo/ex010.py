# Crie um programa que leia quanto dinheiro uma pessoa
# tem na carteira e mostre quantos dólares ela pode
# comprar.

valor = float(input("R$: "))

print('R$ {} = US$ {:.2f}'.format(valor, valor/5.53))