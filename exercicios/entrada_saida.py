"""Exercício simples de entrada, saída e condicionais."""

entrada = input("Você deseja [E]ntrar ou [S]air? ").strip().upper()

if entrada == "E":
    print("Seja bem-vindo!")
elif entrada == "S":
    print("Até a próxima!")
else:
    print("Opção não reconhecida.")
