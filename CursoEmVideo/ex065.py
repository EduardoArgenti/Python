# Crie um programa que leia vários números inteiros pelo
# teclado. No final da execução, mostre a média entre
# todos os valores e qual foi o maior e o menor valores
# lidos. O programa deve perguntar ao usuário se ele quer
# ou não continuar a digitar valores.

soma = count = 0
menor = 99999
maior = -1

#n = int(input('Valor {}: '.format(count+1)))
#op = input('Digitar outro valor? (S/N): ')

op = 'S'

while op not in 'Nn':
    n = int(input('Valor {}: '.format(count + 1)))
    op = input('Digitar outro valor? (S/N): ')
    if n < menor:
        menor = n
    if n > maior:
        maior = n
    count += 1
    soma += n

media = soma / count

print('\nNúmeros digitados: {}.\nSoma total: {}'
      '\nMédia: {}\nMenor: {}\nMaior: {}'.format(count, soma, media, menor, maior))