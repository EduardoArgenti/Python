# Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra "a"
# - Em que posição ela aparece a primeira vez
# - Em que posição ela aparece a última vez

frase = input('Digite uma frase: ')

print('\nAnalisando...')
print(f'"A" aparece {frase.lower().count("a")} vez(es)')
print(f'Primeira vez em: {frase.lower().find("a")+1}')
print(f'Última vez em: {frase.lower().rfind("a")+1}')