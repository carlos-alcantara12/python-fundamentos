texto = "Segurança"
novo_texto = ""

# CORRIGIDO: o loop usava 'texto' (a palavra inteira) dentro do próprio
# loop, em vez de 'letra' (a letra da vez). Além disso, o resultado
# montado em 'novo_texto' nunca era impresso.
for letra in texto:
    novo_texto += "*"

print(novo_texto)
