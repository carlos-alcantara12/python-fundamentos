frase = ('o python é uma linguagem de programação '
         'multiparadigma. '
         'Python foi criado por guido van rossum')

# Utilizamos ".count()" para fazer a contagem de elementos.
print(frase.count('a'))


i = 0
while i < len(frase):
    letra_atual = frase[i]
    print(letra_atual)
    i += 1
