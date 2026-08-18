"""Estrutura de repetição while."""

while True:
    nome = input("Digite seu nome ou 'acabou' para sair: ").strip()

    if nome.lower() == "acabou":
        break

    print(f"Seu nome é {nome.title()}")

print("--- Contagem ---")

contador = 1
while contador <= 5:
    print(contador)
    contador += 1
