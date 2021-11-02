# Adapte o código do desafio 107, criando uma função adicional
# chamada moeda() que consiga mostrar os valores como um valor
# monetário formatado.

from ex108 import moeda

valor = 100
aumento = 0.15
diminuicao = 0.2

print(f'{moeda.moeda(valor)} aumentado em {aumento*100}% = {moeda.moeda(moeda.aumentar(valor, aumento))}')
print(f'{moeda.moeda(valor)} diminuido em {diminuicao*100}% = {moeda.moeda(moeda.diminuir(valor, diminuicao))}')
print(f'O dobro de {moeda.moeda(valor)} = {moeda.moeda(moeda.dobro(valor))}')
print(f'A metade de {moeda.moeda(valor)} = {moeda.moeda(moeda.metade(valor))}')