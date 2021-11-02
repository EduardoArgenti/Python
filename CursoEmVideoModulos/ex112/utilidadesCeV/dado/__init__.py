def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = input(msg).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'ERRO: "{entrada}" é um preço inválido!')
        else:
            valido = True
            return float(entrada)