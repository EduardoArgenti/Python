# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números
# foram digitados e qual foi a soma entre eles (desconsiderando o flag).

count = soma = n = 0
n = int(input('Valor {}: '.format(count + 1)))

while n != 999:
    count += 1
    soma += n
    n = int(input('Valor {}: '.format(count + 1)))

print('\nEncerrado! O usuário digitou {} números.'.format(count))
print('Soma total: {}'.format(soma))