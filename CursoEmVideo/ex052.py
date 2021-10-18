# Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo.

num = int(input('Digite um valor: '))
flag = 0

for i in range(2, num):
    if num % i == 0:
        flag = 1
        break

if flag == 0:
    print(f'{num} é primo!')
else:
    print(f'{num} é composto!')