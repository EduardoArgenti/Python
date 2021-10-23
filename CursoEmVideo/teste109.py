# Modifique as funções que foram criadas no desafio 107 para que elas
# aceitem um parâmetro a mais, informando se o valor retornado por elas
# vai ser ou não formatado pela função moeda(), desenvolvida no ex 108.

from ex109 import moeda

valor = 100
aumento = 0.15
diminuicao = 0.2

print(f'{moeda.moeda(valor)} aumentado em {aumento*100}% = {moeda.aumentar(valor, aumento, format=True)}')
print(f'{moeda.moeda(valor)} diminuido em {diminuicao*100}% = {moeda.diminuir(valor, diminuicao, format=True)}')
print(f'O dobro de {moeda.moeda(valor)} = {moeda.dobro(valor, format=True)}')
print(f'A metade de {moeda.moeda(valor)} = {moeda.metade(valor, format=True)}')