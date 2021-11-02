# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora
# a possibilidade da digitação de um número de tipo inválido. Aproveite e crie
# também uma função leiaFloat() com a mesma funcionalidade.

# Funções
def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO: digite um número inteiro válido!\033[0m')
            continue
        except (KeyboardInterrupt):
            print('\033[1;31mERRO: entrada de dados interrompida!\033[0m')
            break
        else:
            return(num)


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO: digite um número válido!\033[0m')
            continue
        except (KeyboardInterrupt):
            print('\033[1;31mERRO: entrada de dados interrompida!\033[0m')
            break
        else:
            return(num)


# Bloco principal
inteiro = leiaInt('Digite um número inteiro: ')
decimal = leiaFloat('Digite um número decimal: ')
print(f'Número inteiro digitado: {inteiro}')
print(f'Número decimal digitado: {decimal}')