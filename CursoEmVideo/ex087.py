# Aprimore o desafio anterior, mostrando no final:
#
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
soma_pares = soma_terceira_coluna = 0

# Insere valores
for linha in range(0, 3):
    for coluna in range(0, 3):
        n = int(input(f'Posição [{linha+1}][{coluna+1}]: '))
        matriz[linha][coluna] = n

# Percorre a matriz
for linha in range(0, 3):
    for coluna in range(0, 3):
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
        if coluna == 2:
            soma_terceira_coluna += matriz[linha][coluna]
    # Se chegou na terceira linha, significa que temos a segunda linha completa
    if linha == 2:
        maior_valor = matriz[linha-1][0]
        for coluna in range(0, 3):
            if matriz[linha-1][coluna] > maior_valor:
                maior_valor = matriz[linha-1][coluna]




print('=+'*30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end=' ')
    print()
print('=+'*30)
print(f'Soma dos valores pares: {soma_pares}')
print(f'Soma dos valores da terceira coluna: {soma_terceira_coluna}')
print(f'Maior valor da segunda linha: {maior_valor}')