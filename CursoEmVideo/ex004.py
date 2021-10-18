# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele

var = input('Digite algo: ')
print('Tipo primitivo?', type(var))
print('Possui somente espaços?', var.isspace())
print('É numérico?', var.isnumeric())
print('É alfabético?', var.isalpha())
print('É alfanumérico?', var.isalnum())
print('Está em caixa alta?', var.isupper())
print('Está em caixa baixa?', var.islower())
print('Está capitalizada?', var.istitle())
