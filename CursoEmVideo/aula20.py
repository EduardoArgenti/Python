# Funções
def linha(msg):
    print('=' * 30)
    print(f'\t\t{msg}\t\t')
    print('=' * 30)

def soma(a, b, res):
    res = a + b
    return(res)

def contador(* num):
    tam = len(num)
    print(f'Recebi {tam} valores')

def dobra(lista):
    for i in range(0, len(lista)):
        lista[i] *= 2

# Programa principal
linha('FUNÇÃO DE SOMA')

valores = [1, 2, 3, 4, 5]

print(valores)
dobra(valores)
print(valores)



