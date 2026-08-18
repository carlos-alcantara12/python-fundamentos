"""Repete a entrada enquanto a frase começar com a palavra 'erro'."""

while True:
    frase = input("Digite sua frase: ").strip()

    if frase.lower().startswith("erro"):
        print("Entrada inválida. Tente novamente.")
        continue

    print("Sistema válido.")
    break
