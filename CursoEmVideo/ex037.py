# Escreva um programa que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal

num = int(input('Número inteiro: '))
op = int(input('\nEscolha a conversão:\n(1) Binário\n(2) Octal\n(3) Hexadecimal\n'))

if op == 1:
    print('{} em binário: {}'.format(num,bin(num)[2:]))
elif op == 2:
    print('{} em octal: {}'.format(num, oct(num)[2:]))
else:
    print('{} em hexadecimal: {}'.format(num, hex(num)[2:]))


