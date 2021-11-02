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


def resumo(preco=0, aumento=10, reducao=5):
    print('~' * 29)
    print(f'       RESUMO DO VALOR       ')
    print('~' * 29)
    print(f'Preço analisado:\t{moeda(preco)}')
    print(f'Dobro do preço:\t\t{dobro(preco, True)}')
    print(f'Metade do preço:\t{metade(preco, True)}')
    print(f'{aumento}% de aumento:\t\t{aumentar(preco, aumento/100, True)}')
    print(f'{reducao}% de redução:\t\t{diminuir(preco, reducao/100, True)}')
