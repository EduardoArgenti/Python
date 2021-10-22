# Faça um programa que tenha uma lista chamada números
# e duas funções chamadas sorteia() e somaPar(). A primeira
# função vai sortear 5 números e vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores
# pares sorteados pela função anterior.

from random import randint
from time import sleep

# Funções
def sorteia(lista):
    for i in range(0, 5):
        lista.append(randint(0,50))

def somaPar(lista):
    soma_par = 0
    for c in lista:
        if c % 2 == 0:
            soma_par += c
    return(soma_par)


def linha():
    print('-=' * 20)


# Bloco principal
valores = list()
sorteia(valores)
linha()
print('Lista sorteada: ', end='')
for c in valores:
    print(f'{c} ', end='')
    sleep(0.5)
print()
linha()
print(f'Soma dos valores pares: {somaPar(valores)}')
linha()
