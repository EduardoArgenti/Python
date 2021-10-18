# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar
# 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar
# R$ 7,00 por cada Km acima do limite.

velocidade = float(input('Velocidade: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Limite excedido! Sua multa é de R$ {:.2f}'.format(multa))
else:
    print('Você está dentro do limite permitido!')