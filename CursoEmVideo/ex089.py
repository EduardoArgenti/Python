# Crie um programa que leia nome e duas notas de vários alunos
# e guarde tudo em uma lista composta. No final, mostre um
# boletim contendo a média de cada um e permita que o usuário
# possa mostrar as notas de cada aluno individualmente.

alunos_notas = list()
aluno = list()

i = 0
# Cadastramento dos alunos e notas
while True:
    print(f'Aluno {i+1}: ')
    nome = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    # A média já é calculada
    media = (n1 + n2)/2
    aluno.append(nome)
    aluno.append(n1)
    aluno.append(n2)
    aluno.append(media)

    alunos_notas.append(aluno[:])

    op = input('Continuar? (S/N): ')
    if op in 'Nn':
        break

    aluno.clear()
    i += 1

while True:
    op = int(input('\nMenu:\n[ 1 ] Mostrar boletim completo\n[ 2 ] Mostrar notas individual\n[ 3 ] Sair\n'))
    if op == 1:
        print('=*' * 15 + 'BOLETIM' + '=*' * 15)
        for a in alunos_notas:
            print(f'Nome: {a[0]}\nMédia: {a[3]}')
            print('-'*37)
    elif op == 2:
        nome = input('Nome do aluno: ')
        # Considerando que não existam alunos com o mesmo nome
        for a in alunos_notas:
            if a[0] == nome:
                print(f'Nome: {a[0]}\nNota 1: {a[1]}\nNota 2: {a[2]}')
    elif op == 3:
        break