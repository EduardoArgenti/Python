try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Problema encontrado nos tipos de dados inseridos!')
except ZeroDivisionError:
    print('Não é possível dividir um número por 0!')
except KeyboardInterrupt:
    print('Usuário não informou os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'{a} / {b} = {r:.2f}')
    print('Programa concluído')