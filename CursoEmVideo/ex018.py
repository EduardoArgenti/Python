# Faça um programa que leia um ângulo qualquer e mostre na tela
# o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians

ang = float(input('Ângulo: '))
# Para utilizarmos as funções de seno, cosseno e tangente, precisamos
# converter o ângulo de graus para radiano
rad = radians(ang)

seno = sin(rad)
cosseno = cos(rad)
tangente = tan(rad)

print('Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(seno, cosseno, tangente))
