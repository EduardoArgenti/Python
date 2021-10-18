# Escreva um programa que pergunte o salário e calcule o valor de seu aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
# Para inferiores ou iguais o aumento é de 15%.

salario = float(input('Salário: '))

if salario > 1250:
    aumento = salario * 0.1
else:
    aumento = salario * 0.15

print(f'Novo salário: R$ {salario + aumento}')