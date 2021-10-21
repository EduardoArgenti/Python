# Crie um programa que leia nome, ano de nascimento e carteira
# de trabalho e cadastre-o (com idade) em um dicionário. Se por
# acaso a CTPS for diferente de ZERO, o dicionário receberá
# também o ano de contratação e o salário. Calcule e acrescente,
# além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

funcionario = dict()

funcionario['nome'] = input('Nome: ')
funcionario['ano_nasc'] = int(input('Ano de nascimento: '))
funcionario['idade'] = datetime.now().year - funcionario['ano_nasc']
funcionario['cpts'] = int(input('Carteira de trabalho: '))
if funcionario['cpts'] != 0:
    funcionario['ano_cont'] = int(input('Ano de contratação: '))
    funcionario['salario'] = float(input('Salário: '))
    funcionario['idade_aposentadoria'] = funcionario['idade'] + ((funcionario['ano_cont'] + 35) - datetime.now().year)

for k, v in funcionario.items():
    print(f'{k}: {v}')