# Faça um programa que tenha uma função notas() que pode
# receber várias notas de alunos e vai retornar um dicionário
# com as seguintes informações:
#
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional) com algo como sit=True
#
# Adicione também os docstrings da função

# Função
def notas(* notas, sit=False):
    """
    Função que recebe uma quantidade variável de notas, as analisa
    e guarda as informações em um dicionário, retornando-o.
    :param notas: obrigatório haver pelo menos uma nota.
    :param sit: opcional, se for True, guarda também a situação da média.
    :return: retorna o dicionário com as informações processadas.
    """
    informacoes = dict()
    soma = 0

    for n in notas:
        soma += n
    media = soma / len(notas)

    informacoes['maior_nota'] = max(notas)
    informacoes['menor_nota'] = min(notas)
    informacoes['media'] = media
    if sit:
        if media < 4:
            informacoes['situacao'] = 'REPROVADO'
        elif 4 <= media < 7:
            informacoes['situacao'] = 'RECUPERAÇÃO'
        elif 7 <= media < 10:
            informacoes['situacao'] = 'APROVADO'
        else:
            informacoes['situacao'] = 'APROVADO COM EXCELÊNCIA'


    return(informacoes)


# Bloco principal
print(notas(1, sit=True))

