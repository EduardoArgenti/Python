# Faça um programa que leia o sexo de uma pessoa, mas
# só aceite os valores ‘M’ ou ‘F’. Caso esteja errado,
# peça a digitação novamente até ter um valor correto.

flag = 1

while flag == 1:
    sexo = input('Sexo (M/F): ').strip()
    if sexo in 'MF':
        flag = 0

print('Dado inserido com sucesso!')
print('Valor:', sexo)