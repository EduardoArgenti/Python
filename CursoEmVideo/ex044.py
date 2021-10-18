# Elabore um programa que calcule o valor a ser pago por um
# produto, considerando seu preço normal e condição de pagamento:
# - Á vista dinheiro/cheque: 10% de desconto
# - Á vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais vezes no cartão: 20% de juros

preco = float(input('Preço: '))
op = int(input('''(1) Á vista dinheiro/cheque
(2) Á vista no cartão\n(3) E até 2x no cartão\n(4) 3x ou mais no cartão\nOpção: '''))

print('\n')
if op == 1:
    print('10% de desconto!\nTotal: R$ {:.2f}'.format(preco * 0.9))
elif op == 2:
    print('5% de desconto!\nTotal: R$ {:.2f}'.format(preco * 0.95))
elif op == 3:
    print('Preço normal.\nTotal: R$ {:.2f}'.format(preco))
else:
    print('Preço com juros!\nTotal: R$ {:.2f}'.format(preco * 1.2))
