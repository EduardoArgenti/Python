# Desenvolva um programa que leia o comprimento de três retas e diga
# ao usuário se elas podem ou não formar um triângulo.

a = int(input('Lado A: '))
b = int(input('Lado B: '))
c = int(input('Lado C: '))

if a + b >= c and a + c >= b and b + c >= a:
    print('\nOs lados digitados formam um triângulo!')
else:
    print('\nOs lados digitados NÃO formam um triângulo!')