"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver
4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras,
escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é grande".
"""

nome = input('Qual é o seu nome?: ')
tamanho = len(nome)

if nome.isalpha():
    if tamanho <= 4:
        print('Seu nome é curto')
    elif 5 <= tamanho <= 6:
        print('Seu nome é normal')
    elif tamanho > 6:
        print('Seu nome é grande')
else:
    print('Digite um nome válido!')

