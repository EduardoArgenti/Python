# Crie um programa onde o usuário digite uma expressão
# qualquer que use parênteses. Seu aplicativo deverá
# analisar se a expressão passada está com os parênteses
# abertos e fechados na ordem correta.

expressao = input('Expressão matemática: ')
pilha = []

for c in expressao:
    if c == '(':
        pilha.append('(')
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Expressão correta!')
else:
    print ('Expressão incorreta!')