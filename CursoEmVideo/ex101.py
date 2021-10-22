# Crie um programa que tenha uma função chamada voto() que vai
# receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto
# NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

from datetime import datetime

# Função
def voto(ano_nasc):
    idade = datetime.now().year - ano_nasc

    saida = f'Idade: {idade}\t'

    if idade < 16:
        saida += 'VOTO NEGADO'
    elif 16 <= idade < 18 or idade > 70:
        saida += 'VOTO OPCIONAL'
    elif 18 <= idade <= 70:
        saida += 'VOTO OBRIGATÓRIO'

    return(saida)


# Bloco principal
ano = int(input('Qual é o seu ano de nascimento?: '))
print('-=' * 30)
print(voto(ano))
print('-=' * 30)
