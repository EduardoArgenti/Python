# Refaça o desafio 035 dos triângulos, acrescentando o recurso
# de mostrar que tipo de triângulo será formado:
# - Equilátero
# - Isósceles
# - Escaleno

a = int(input('Lado A: '))
b = int(input('Lado B: '))
c = int(input('Lado C: '))

if a + b >= c and a + c >= b and b + c >= a:
    if a == b == c:
        print('\nTriângulo equilátero!')
    elif a != b != c != a:
        print('\nTriângulo escaleno!')
    else:
        print('\nTriângulo isósceles!')
else:
    print('\nOs lados digitados NÃO formam um triângulo!')