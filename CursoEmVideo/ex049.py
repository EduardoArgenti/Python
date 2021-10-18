# Refaça o DESAFIO 9, mostrando a tabuada de um número
# que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Digite um valor: '))

for i in range(1,11):
    print(f'{num} X {i} = {num*i}')