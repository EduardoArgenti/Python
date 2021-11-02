# Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
# descrito, exiba a saudação apropriada. Ex: Bom dia 0-11, Boa tarde 12-17 e
# Boa noite 18-23

horas = input('Que horas são?: ')

if horas.isdigit():
    horas = int(horas)

    if horas < 0 or horas > 23:
        print('As horas devem estar entre 0 e 23')
    else:
        if 0 <= horas <= 11:
            print('Bom dia!')
        elif 12 <= horas <= 17:
            print('Boa tarde!')
        elif 18 <= horas <= 23:
            print('Boa noite!')
else:
    print('Digite um horário entre 0 e 23.')
