frase = ('o python é uma linguagem de programação '
         'multiparadigma. '
         'Python foi criado por guido van rossum')

# Utilizamos ".count()" para fazer a contagem de elementos.
print(frase.count('a'))

# CORRIGIDO: 'print(letra_atual)' e 'i += 1' estavam sem indentação,
# ou seja, fora do corpo do while. Como 'i' nunca era incrementado
# dentro do loop, isso causava um loop infinito.
i = 0
while i < len(frase):
    letra_atual = frase[i]
    print(letra_atual)
    i += 1
