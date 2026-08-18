"""Exercício de manipulação e validação básica de strings."""

nome = input("Digite seu nome: ").strip()
idade = input("Digite sua idade: ").strip()

if nome and idade:
    nome_invertido = nome[::-1]
    total_letras = len(nome.replace(" ", ""))

    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome_invertido}")
    print("Seu nome contém espaços." if " " in nome else "Seu nome não contém espaços.")
    print(f"Seu nome possui {total_letras} letras.")
    print(f"A primeira letra do seu nome é: {nome[0]}")
    print(f"A última letra do seu nome é: {nome[-1]}")
else:
    print("Você não forneceu todas as informações necessárias.")
