# Crie um programa que declare uma matriz de dimensão 3×3
# e preencha com valores lidos pelo teclado. No final,
# mostre a matriz na tela, com a formatação correta.

# Outra forma de fazer é receber valores [[0, 0, 0], [0, 0, 0], [0, 0, 0]
# para não precisar utilizar o append, apenas atribuições simples direto
# na coordenada.
matriz = [[], [], []]

for linha in range(0, 3):
    for coluna in range(0, 3):
        n = int(input(f'Posição [{linha+1}][{coluna+1}]: '))
        matriz[linha].append(n)

print('=+'*30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end=' ')
    print()