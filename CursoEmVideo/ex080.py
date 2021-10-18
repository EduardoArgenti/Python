# Crie um programa onde o usuário possa digitar cinco
# valores numéricos e cadastre-os em uma lista, já
# na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

from random import randint

aleatorios = list()
valores = list()

for c in range(0, 5):
    # n = int(input(f'Valor {c+1}: '))
    n = randint(0, 20)
    aleatorios.append(n)

    # Lista vazia
    if len(valores) == 0:
        valores.append(n)
    # Lista com 1 elemento
    elif len(valores) == 1:
        if n >= valores[0]:
            valores.append(n)
        else:
            valores.insert(0, n)
    # Lista com 2 ou mais elementos
    else:
        if n <= valores[0]:
            valores.insert(0, n)
        elif n >= valores[-1]:
            valores.append(n)
        # Se o elemento não será inserido à esquerda ou à direita da lista, inserimos no meio.
        else:
            i = 1
            while i < len(valores):
                if n <= valores[i]:
                    valores.insert(i, n)
                    break
                i += 1

print(f'Lista original: {aleatorios}')
print(f'Lista ordenada: {valores}')