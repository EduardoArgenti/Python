# Escreva um programa que converta uma temperatura digitando em
# graus Celsius e converta para graus Fahrenheit.

temp_c = float(input('Temperatura em Celsius: '))

temp_f = (temp_c * 9)/5 + 32

print(f'{temp_c}ºC = {temp_f}ºF')
