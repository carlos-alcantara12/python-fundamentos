palavra_secreta = "coragem"
numero_tentativas = 0
letras_acertadas = ""

while True:
    palpite = input("Escreva uma letra: ").lower()

    # Parte 2: Validação
    if len(palpite) > 1:
        print("Digite apenas uma letra.")
        continue

    numero_tentativas += 1
    print(f"Tentativa número {numero_tentativas}")           

    # Parte 3: Guardar acertos e montar a palavra
    if palpite in palavra_secreta:
        letras_acertadas += palpite

    palavra_formada = ""
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"

    print("Palavra formada:", palavra_formada)

    # Parte 4: Condição de vitória
    if palavra_formada == palavra_secreta:
        print("Parabéns, você acertou !!!")
        print(f"A palavra secreta era : {palavra_secreta}")
        print(f"Número de tentativas necessárias : {numero_tentativas}")
        break

