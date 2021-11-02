num1 = input('Valor 1: ')
num2 = input('Valor 2: ')

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
else:
    print('Os valores digitados não são numéricos!')
