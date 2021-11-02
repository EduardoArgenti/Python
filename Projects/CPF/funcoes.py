from random import randint

# Remove o ponto e hífen do CPF.
def removerFormatacaoCpf(cpf):
    resultado = cpf.replace(".", "")
    resultado = resultado.replace("-", "")

    return resultado


# Adiciona o ponto e hífen no CPF.
def adicionarFormatacaoCpf(cpf):
    cpfFormatado = ''

    cpfFormatado += cpf[:3]
    cpfFormatado += '.'
    cpfFormatado += cpf[3:6]
    cpfFormatado += '.'
    cpfFormatado += cpf[6:9]
    cpfFormatado += '-'
    cpfFormatado += cpf[9:]

    return cpfFormatado


# Versão 2, mais otimizada e menos verbosa. Trabalha com CPFs
# sem os 2 dígitos.
def calcularDigitosCpf(cpf):
    digitos = [str(0), str(0)]

    for i in range(2):
        soma = 0
        for k, v in enumerate(range(10+i, 1, -1)):
            soma += int(cpf[k]) * v

        calculo = 11 - (soma % 11)
        if calculo > 9:
            digitos[i] = str(0)
        else:
            digitos[i] = str(calculo)

        if i == 0:
            cpf += str(digitos[i])

    return digitos


def validarCpf(cpf):
    # Não passa os 2 últimos dígitos.
    temp = cpf[:-2]

    digitos = calcularDigitosCpf(temp)
    temp += ''.join(digitos)

    if temp == cpf:
        valido = True
    else:
        valido = False

    return valido


def gerarCpf():
    cpf = ''

    for i in range(0, 9):
        cpf += str(randint(0, 9))

    digitos = calcularDigitosCpf(cpf)

    cpf += ''.join(digitos)
    cpf = adicionarFormatacaoCpf(cpf)

    return cpf



