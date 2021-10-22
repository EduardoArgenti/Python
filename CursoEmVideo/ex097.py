# Faça um programa que tenha uma função chamada escreva()
# que recebe um texto qualquer como parâmetro e mostre uma mensagem
# com tamanho adaptável.

# As linhas de cima e de baixo acompanham o tamanho do texto!

# Função
def escreva(mensagem):
    tam = len(mensagem)
    print('~' * (tam+4))
    print(f'{" "*2}{mensagem}{" "*2}')
    print('~' * (tam+4))


# Bloco principal
texto = input('Digite uma mensagem: ')

escreva(texto)