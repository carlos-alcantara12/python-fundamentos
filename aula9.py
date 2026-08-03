#Operadores lógicos: (or)

acesso = input("Você deseja [E]ntrar ou [S]air? ")

# 1. Portão principal (Repare nos 4 espaços de recuo nas linhas de dentro)
if acesso == "E" or acesso == "e":
    nome = input("Digite o nome do usuário: ")
    senha = input('Digite a senha: ') # CORRIGIDO: sem int() para funcionar com texto
    senha_permitida = "3301"
    
    # Este if está dentro do primeiro, então ele ganha +4 espaços de recuo (8 no total)
    if senha == senha_permitida:
        print(f'Seja bem-vindo, {nome}!') # CORRIGIDO: adicionado o f antes das aspas
    else:
        print("Senha incorreta, acesso negado.")

# CORRIGIDO: mudamos de 'if' para 'elif' para que o Python só teste isso se o primeiro der falso
elif acesso == "S" or acesso == "s":
    print('Até a próxima')

# O else final só roda se o usuário não digitou nem E, nem S
else:
    print("Opção inválida, digite E ou S.")
