# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar
# - Se já passou do tempo do alistamento
# - Seu programa também deverá mostrar o tempo que falta ou que
# passou do prazo
from datetime import datetime

ano = int(input('Ano de nascimento: '))
idade = datetime.now().year - ano

if idade < 18:
    print('\nVocê ainda vai se alistar daqui {} anos!'.format(18 - idade))
elif idade > 18:
    print('\nVocê chegou {} anos atrasado!'.format(idade - 18))
else:
    print('\nJá é hora de se alistar!')