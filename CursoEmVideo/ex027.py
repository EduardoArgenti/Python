# Faça um programa que leia o nome completo de uma pessoa, mostrando
# em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza => primeiro = Ana; segundo = Souza

nome = input('Nome: ')
nome_separado = nome.split()

print(f'\nPrimeiro nome: {nome_separado[0]}')
print(f'\nÚltimo nome: {nome_separado[-1]}')