nome = input("Digite seu nome: ").strip()
idade = input("Digite sua idade: ").strip() # CORRIGIDO: sem int() para aceitar validação de vazio

if nome != "" and idade != "":
    print(f"Seu nome é {nome}")
    
    # Repare que todas as linhas abaixo ganharam espaços para ficar DENTRO do if
    nome_invertido = nome[::-1]
    print(f"Seu nome invertido é {nome_invertido}") # CORRIGIDO: erro de digitação 'inertido'
    
    if " " in nome:
        print('Seu nome contem espaços.')
    else:
        print('Seu nome não contém espaços')
        
    total_letras = len(nome.replace(" ", "")) # CORRIGIDO: ordem do replace para remover espaços
    print(f"Seu nome possui o total de letras = {total_letras}")
    
    # CORRIGIDO: Adicionado o 'f' antes das aspas e removido o espaço antes do [0]
    print(f"A primeira letra do seu nome é: {nome[0]}")
    print(f"A última letra de seu nome é: {nome[-1]}")

else: # Agora o else funciona, porque o if principal está conectado a ele!
    print("Desculpe, você não forneceu as informações necessárias.")