# Faça um programa que leia o comprimento do cateto oposto
# e co cateto adjacente de um triângulo retângulo, calcule
# e mostre o comprimento da hipotenusa.
from math import sqrt, pow, trunc

co = int(input('Cateto  oposto: '))
ca = int(input('Cateto adjacente: '))

hipotenusa = sqrt(pow(co,2) + pow(ca,2))

print(f'A hipotenusa é {trunc(hipotenusa)}')