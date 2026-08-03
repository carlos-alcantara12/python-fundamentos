# Começamos com um laço verdadeiro para que o programa já entre aqui

while True:
    frase = input("Digite sua frase: ")

    # Coloquei uma verificação para identificar se a frase começa com "erro"
    # e, se começar, converto sempre para minúsculo com lower().
    # também adicionei o (continue) para que o programa siga rodando.

   
    if frase.lower().startswith('erro'):
        print("Erro!!!, não aceitamos erros aqui.")
        continue

    # Caso a resposta do usuário não caia no erro o programa exibe o print abaixo:
    print("Sistema Válido.")














