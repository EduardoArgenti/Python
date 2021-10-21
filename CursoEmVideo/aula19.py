estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = input('Unidade federativa: ')
    estado['sigla'] = input('Sigla: ')
    brasil.append(estado.copy())

for estado in brasil:
    for k, v in estado.items():
        print(f'Campo {k}: {v}')