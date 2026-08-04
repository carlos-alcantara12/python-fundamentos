# Começamos com um laço verdadeiro para que o programa já entre aqui

while True:
    frase = input("Digite sua frase: ")

    # Coloquei uma verificação para identificar se a frase começa com "erro"
    # e, se começar, converto sempre para minúsculo com lower().
    # também adicionei o (continue) para que o programa siga rodando.

    # CORRIGIDO: a frase já era convertida para minúsculo com .lower(),
    # mas a comparação usava 'Erro' com E maiúsculo. Como uma string
    # minúscula nunca começa com 'Erro' (maiúsculo), essa condição
    # nunca era verdadeira.
    if frase.lower().startswith('erro'):
        print("Erro!!!, não aceitamos erros aqui.")
        continue

    # Caso a resposta do usuário não caia no erro o programa exibe o print abaixo:
    print("Sistema Válido.")
