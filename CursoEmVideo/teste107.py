# Crie um módulo chamado moeda.py que tenha as funções incorporadas
# aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importa esse módulo e use algumas dessas funções.

from ex107 import moeda

valor = 100
aumento = 0.15
diminuicao = 0.2

print(f'{valor} aumentado em {aumento*100}% = {moeda.aumentar(valor, aumento)}')
print(f'{valor} diminuido em {diminuicao*100}% = {moeda.diminuir(valor, diminuicao)}')
print(f'O dobro de {valor} = {moeda.dobro(valor)}')
print(f'A metade de {valor} = {moeda.metade(valor)}')