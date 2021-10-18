# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input('Digite um número: '))
count = num
resultado = 1
print('\n{}! ='.format(num), end='')
while count != 0:
    if count == 1:
        print(' {} = '.format(count), end='')
    else:
        print(' {} X'.format(count), end='')
    resultado *= count
    count -= 1
print(resultado)
