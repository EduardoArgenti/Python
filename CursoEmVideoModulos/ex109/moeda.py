def aumentar(valor, aumento, format=False):
    resultado = valor * (1 + aumento)
    return resultado if format == False else moeda(resultado)


def diminuir(valor, diminuicao, format=False):
    resultado = valor * (1 - diminuicao)
    return resultado if format == False else moeda(resultado)


def dobro(valor, format=False):
    resultado = valor * 2
    return resultado if format == False else moeda(resultado)


def metade(valor, format=False):
    resultado = valor / 2
    return resultado if format == False else moeda(resultado)


def moeda(valor):
    return f'R$ {valor:.2f}'.replace('.', ',')