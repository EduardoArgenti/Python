# Faça um programa que tenha uma função maior(), que
# receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos e dizer qual deles
# é o maior.

# Função
def maior(* num):
    return(max(num))


# Bloco principal
print(maior(27, 1, 2, 3, 4, 5))
