# Crie um programa que tenha uma dupla totalmente preenchida
# com uma contagem por extenso, de zero até vinte. Seu programa
# deverá ler um número pelo teclado (entre 0 e 20) e
# mostrá-lo por extenso.

numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
           'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
           'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis',
           'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

num = int(input('Número (de 0 a 20): '))

while num < 0 or num > 20:
    num = int(input('Número inválido! Tente novamente (de 0 a 20): '))

print(f'{num} lê-se como {numeros[num]}')

