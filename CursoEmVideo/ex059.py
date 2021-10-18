# Crie um programa que leia dois valores e mostre um menu na tela:
#
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
#
# Seu programa deverá realizar a operação solicitada em cada caso.

a = int(input('A: '))
b = int(input('B: '))
op = int(input('\n[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair'))

while op != 5:
    if 1 <= op <= 5: # Verifica opção válida
        if op == 1:
            print('\n{} + {} = {}'.format(a, b, a+b))
        elif op == 2:
            print('\n{} X {} = {}'.format(a, b, a*b))
        elif op == 3:
            if a > b:
                print('{} é maior que {}'.format(a, b))
            elif a == b:
                print('{} e {} são iguais'.format(a, b))
            else:
                print('{} é maior que {}'.format(b, a))
        elif op == 4:
            a = int(input('A: '))
            b = int(input('B: '))
    else:
        print('Opção inválida! Tente novamente.')
    op = int(input('\n[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair'))
print('\nPrograma finalizado!')
