# Crie um programa que leia uma frase qualquer e diga
# se ela é um palíndromo, desconsiderando os espaços.

frase = input('Digite uma frase: ')
sem_espacos = frase.split()
junto = ''.join(sem_espacos)

print(junto)

if junto.lower() == junto[::-1].lower():
    print(f'"{frase}" é um palíndromo!')
else:
    print(f'"{frase}" NÃO é um palíndromo!')