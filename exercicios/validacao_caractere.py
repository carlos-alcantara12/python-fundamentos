"""Valida se o usuário informou exatamente um caractere."""

while True:
    caractere = input("Digite um caractere: ").strip()

    if len(caractere) != 1:
        print("Digite exatamente um caractere.")
        continue

    print(f"Caractere '{caractere}' válido.")
    break
