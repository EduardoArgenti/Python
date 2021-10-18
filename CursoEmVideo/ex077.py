# Crie um programa que tenha uma tupla com várias palavras
# (não usar acentos). Depois disso, você deve mostrar,
# para cada palavra, quais são as suas vogais.

palavras = ('Eu', 'estou', 'adorando', 'aprender', 'Python!')

for pos, c in enumerate(palavras):
    print(f'Vogais da palavra "{palavras[pos]}": ', end='')
    for i, letra in enumerate(palavras[pos]):
        if letra in 'AaEeIiOoUu':
            print(f'{letra}', end=' ')
    print()
