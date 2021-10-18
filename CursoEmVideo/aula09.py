frase = 'Curso em Vídeo Python'

print('\nAnalisando textos: ')
print(len(frase))
print(frase.count('o'))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)

print('\nTransformando textos: ')
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

frase_espacos = '   Aprendendo Python!  '
print(frase_espacos)
print(frase_espacos.strip())

print('\nDividindo Strings: ')
palavras_frase = frase.split()
print(palavras_frase)
frase_tracos = '-'.join(palavras_frase)
print(frase_tracos)