# Escreva um programa para aprovar o empréstimo bancário para a compra
# de uma casa. O programa vai perguntar o valor da casa, o salário do
# comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder
# 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Valor da casa: '))
salario = float(input('Salário: '))
anos = int(input('Anos: '))

qtd_prestacoes = anos * 12
valor_prestacao = valor_casa/qtd_prestacoes

if valor_prestacao <= salario * 0.3:
    print('\nPrestação: R$ {:.2f}'.format(valor_prestacao))
else:
    print('\nEmpréstimo negado! Salário insuficiente para aprovação.')