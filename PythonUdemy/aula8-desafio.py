
from datetime import datetime

nome = str(input('Nome: '))
idade = int(input('Idade: '))
altura = float(input('Altura: '))
peso = float(input('Peso: '))
ano_nasc = datetime.now().year - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos, {altura}m de altura e pesa {peso}kg.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {ano_nasc}')

num_1 = 2
num_2 = '2'
num_3 = num_1 + num_2
print(num_3)