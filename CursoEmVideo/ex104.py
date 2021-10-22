# Crie um programa que tenha a função leiaInt(), que vai funcionar
# de forma semelhante à função input() do Python, só que fazendo
# a validação para aceitar apenas um valor numérico.
#
# Ex: n = leiaInt('Digite um n: ')

# Função
def leiaInt(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            break
        else:
            print(f'\033[1:31mO valor deve ser numérico! Tente novamente.\033[0m')
    return(num)


# Bloco principal
n = leiaInt('Digite um número: ')
print(f'Número digitado: {n}')