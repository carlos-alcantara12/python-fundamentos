#Operadores lógicos: (and)

idade = int(input("Digite sua idade:"))
renda = float(input("Digite sua renda:"))
nome_limpo = input("Seu nome esta limpo?, digite [S]im ou [N]ão:").strip().upper()

if idade >= 18 and renda >= 2500 and nome_limpo == "S":
    print("Empréstimo aprovado.")
else:
    print("Empréstimo negado!, você não possui todos os requisitos")
