# Faça um programa que peça ao usuário para digitar um número inteiro e
# que informa se ele é par ou ímpar. Se não for um número inteiro, avise
# o usuário.

num = input('Digite um número inteiro: ')

if num.isdigit():
    num = int(num)

    if num % 2 == 0:
        print(f'{num} é par!')
    else:
        print(f'{num} é ímpar!')

else:
    print('O valor digitado não é um número inteiro!')