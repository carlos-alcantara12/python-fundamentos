"""Jogo simples de descoberta de uma palavra secreta."""

palavra_secreta = "coragem"
tentativas = 0
letras_tentadas = set()

while True:
    palpite = input("Digite uma letra: ").strip().lower()

    if len(palpite) != 1 or not palpite.isalpha():
        print("Digite exatamente uma letra.")
        continue

    if palpite in letras_tentadas:
        print("Você já tentou essa letra.")
        continue

    letras_tentadas.add(palpite)
    tentativas += 1

    palavra_formada = ""
    for letra in palavra_secreta:
        palavra_formada += letra if letra in letras_tentadas else "*"

    print("Palavra formada:", palavra_formada)

    if palavra_formada == palavra_secreta:
        print("Parabéns, você acertou!")
        print(f"A palavra secreta era: {palavra_secreta}")
        print(f"Número de tentativas: {tentativas}")
        break
