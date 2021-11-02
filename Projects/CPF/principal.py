from funcoes import removerFormatacaoCpf, adicionarFormatacaoCpf, calcularDigitosCpf, validarCpf, gerarCpf

# Apenas o primeiro CPF é inválido
cpfsOriginais = ['444.341.918-22', # CPF INVÁLIDO
                 '351.871.470-80',
                 '267.314.820-56',
                 '609.934.279-60']

cpfsValidos = []

# Validar CPFs
for item in cpfsOriginais:
    temp = removerFormatacaoCpf(item)
    if validarCpf(temp):
        cpfsValidos.append(adicionarFormatacaoCpf(temp))


# Gera 100 CPFs válidos e os acrescenta na lista.
# Não é necessário validar pois o cálculo dos
# dois dígitos já é realizado na geração do CPF.
for i in range(0, 100):
    cpfsValidos.append(gerarCpf())

# Imprimir a lista de CPFs válidos
for i in cpfsValidos:
    print(i)





