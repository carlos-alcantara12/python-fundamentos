"""Operador lógico `or` e estruturas condicionais."""

acesso = input("Você deseja [E]ntrar ou [S]air? ").strip().upper()

if acesso == "E":
    nome = input("Digite o nome do usuário: ").strip()
    senha = input("Digite a senha: ")
    senha_permitida = "3301"

    if senha == senha_permitida:
        print(f"Seja bem-vindo, {nome}!")
    else:
        print("Senha incorreta, acesso negado.")
elif acesso == "S":
    print("Até a próxima.")
else:
    print("Opção inválida. Digite E ou S.")
