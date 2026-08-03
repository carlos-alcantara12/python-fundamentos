while True:
    caractere = input("Digite o caractere que deseja esconder:")

    if len(caractere) != 1:
        print("Quantidade de caracteres inválidas.")
        continue

    print(f"Caractere {caractere} válido")
    break
