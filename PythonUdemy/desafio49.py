"""
Validar CPFs.
"""

def removeCaracteresEspeciais(cpf):
    resultado = cpf.replace(".", "")
    resultado = resultado.replace("-", "")

    return resultado

# Versão 2, mais otimizada e menos verbosa. Trabalha com CPFs
# sem os 2 dígitos.
def calculaDigito_v2(cpf):
    digitos = [0, 0]

    for i in range(2):
        soma = 0
        for k, v in enumerate(range(10+i, 1, -1)):
            soma += int(cpf[k]) * v

        calculo = 11 - (soma % 11)
        if calculo > 9:
            digitos[i] = 0
        else:
            digitos[i] = calculo

        if i == 0:
            cpf += str(digitos[i])

    return digitos

def calculaDigito(cpf, modo):
    soma = 0
    # Calcula o primeiro dígito
    if modo == 1:
        for k, v in enumerate(range(10, 1, -1)):
            soma += int(cpf[k]) * v

        calculo = 11 - (soma % 11)
        if calculo > 9:
            resultado = 0
        else:
            resultado = calculo
    # Calcula o segundo dígito
    elif modo == 2:
        for k, v in enumerate(range(11, 1, -1)):
            soma += int(cpf[k]) * v
            print(cpf[k], v, int(cpf[k]) * v)

        calculo = 11 - (soma % 11)

        if calculo > 9:
            resultado = 0
        else:
            resultado = calculo

    return resultado


# cpf = input('Informe seu CPF: ')
cpf = '446.341.918-22'
cpf = cpf.replace(".", "")
cpf = cpf.replace("-", "")

"""
Primeira versão

# Comparando o CPF informado com o calculado
digitos = [calculaDigito(cpf, 1), calculaDigito(cpf, 2)]

if int(cpf[-2]) == digitos[0] and int(cpf[-1]) == digitos[1]:
    print('CPF válido!')
    print(f'Original: -{cpf[-2]}{cpf[-1]} -> Calculado: -{digitos[0]}{digitos[1]}')
else:
    print('CPF inválido!')
    print(f'Original: -{cpf[-2]}{cpf[-1]} -> Calculado: -{digitos[0]}{digitos[1]}')
"""

cpf1 = removeCaracteresEspeciais('446.341.919-22')
cpf2 = removeCaracteresEspeciais('351.871.470-80')
cpf3 = removeCaracteresEspeciais('267.314.820-56')
cpf4 = '150724818'

# Remover os dois dígitos
cpf1 = cpf1[:-2]
cpf2 = cpf2[:-2]
cpf3 = cpf3[:-2]

print(calculaDigito_v2(cpf1))
print(calculaDigito_v2(cpf2))
print(calculaDigito_v2(cpf3))
print(calculaDigito_v2(cpf4))

