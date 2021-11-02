def aumentar(valor, aumento):
    resultado = valor * (1 + aumento)
    return resultado


def diminuir(valor, diminuicao):
    resultado = valor * (1 - diminuicao)
    return resultado


def dobro(valor):
    resultado = valor * 2
    return resultado


def metade(valor):
    resultado = valor / 2
    return resultado


def moeda(valor):
    return f'R$ {valor:.2f}'.replace('.', ',')