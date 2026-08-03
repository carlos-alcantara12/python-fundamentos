#Estrutura de repetição (while)
# while -> (enquanto)
# Executa uma ação enquanto uma condição for verdadeira

condicao = True

while condicao:
    nome = input('Digite seu nome:').capitalize()
    print(f"Seu nome é {nome}")

    if nome == "Acabou":
        break

#----------------------------------------------------------


contador = 0

while contador < 0:
    contador = contador + 1
    print(contador)

print("OI")
