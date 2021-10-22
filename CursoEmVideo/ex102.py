# Crie um programa que tenha uma função fatorial()
# que receba dois parâmetros: o primeiro que indique
# o número a calcular e o outro chamado show, que será
# um valor lógico (opcional) indicando se será mostrado
# ou não na tela o processo de cálculo do fatorial.
#
# Também deve ter uma docstring ensinando a usar a função!

# Função
def fatorial(valor, show=False):
    """
    Função que calcula o fatorial de um valor informado e pode
    ou não mostrar o cálculo por extenso, de maneira didática.
    :param valor: o número cujo fatorial será calculado.
    :param show: operador lógico opcional. Se for True, mostra o cálculo
    :return: retorna string contendo o valor formatado
    """

    resultado = 1
    retorno = ''
    resposta_completa = f'{valor}! = '

    for i in range(valor, 0, -1):
        resultado *= i
        # Mostrar cálculo
        if show:
            if i > 1:
                resposta_completa += f' {i} X'
            else:
                resposta_completa += f' {i} = {resultado}'

    if show:
        return(resposta_completa)
    else:
        return(f'{valor}! = {resultado}')


# Bloco principal
print(fatorial(5, False))
help(fatorial)
