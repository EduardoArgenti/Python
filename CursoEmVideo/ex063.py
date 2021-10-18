# Escreva um programa que leia um número N inteiro qualquer e
# mostre na tela os N primeiros elementos de uma Sequência
# de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8

n = int(input('N elementos de Fibonacci: '))

anterior = 0
atual = 1

print('{} {} '.format(anterior, atual), end='')

count = 0
while count < n - 2:
    proximo = anterior + atual
    anterior = atual
    atual = proximo
    print('{} '.format(proximo), end='')
    count += 1