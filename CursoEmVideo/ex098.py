# Faça um programa que tenha uma função chamada contador(), que receba
# três parâmetros: início, fim e passo e realize a contagem.
# Seu programa tem que realizar três contagens através da função criada:
#
# a) De 1 até 10, de 1 em 1
# b) De 10 até 0, de 2 em 2
# c) Uma contagem personalizada.

from time import sleep

# Funções
def contador(inicio, fim, passo):

    if passo == 0:
        passo = 1
    elif passo < 0:
        passo *= -1

    if inicio < fim:
        i = inicio
        for i in range(inicio, fim + 1, passo):
            print(f'{i} ', end='')
            #sleep(0.25)
        print()
    elif inicio > fim:
        i = inicio
        for i in range(inicio, fim - passo, -1 * passo):
            print(f'{i} ', end='')
            #sleep(0.25)
        print()

def imprimeLinha():
    print('-=' * 30)


# Bloco principal
print('Contagem de 1 até 10 de 1 em 1')
imprimeLinha()
contador(1, 10, 1)
imprimeLinha()
print('Contagem de 10 até 0 de 2 em 2')
imprimeLinha()
contador(10, 1, 2)
imprimeLinha()

print('Contagem personalizada!')
imprimeLinha()
ini = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)

