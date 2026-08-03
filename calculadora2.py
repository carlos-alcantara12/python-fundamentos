print("=== CALCULADORA 2 ===")

while True:
    
    # PEDINDO OS DADOS DO USUÁRIO E DEMONSTRANDO OS OPERADORES:
    # Removemos o 'int()' daqui para o try/except poder fazer o seu trabalho!
    numero1 = input("Digite um valor: ")
    numero2 = input("Digite o segundo valor: ")
    operadores = input("Digite um operador: (+, -, *, /) ")
    
    # É nesta parte onde o programa testa o que o usuário escreveu
    # e tenta validar em True or False. Se for True o mesmo valida 
    # o número e segue para a conta, se der False o programa não falha
    # de uma vez, ele repete a ação de pedir para o usuário digitar algum valor:

    try:
        # Usando as mesmas variáveis que você coletou lá em cima!
        numero1 = float(numero1)
        numero2 = float(numero2) 
        numeros_validos = True
    
    except ValueError:
        numeros_validos = False

    if not numeros_validos:
        print("Erro: um ou ambos os dados fornecidos não são números. Digite apenas números!")
        print("-" * 30)
        continue

    # Aqui eu estou fazendo uma verificação dos operadores e suas quantidades.
    # Se o usuário digitar algum operador não permitido ou digitar mais de um
    # o programa vai apresentar esta mensagem abaixo:
    
    operadores_permitidos = ["+", "-", "*", "/"]
    if operadores not in operadores_permitidos or len(operadores) > 1:
        print("Erro: Digite apenas um operador válido (+, -, *, /)")
        print("-" * 30)
        continue

    # Aqui eu estou realizando os calculos dos dados fornecidos pelos usuários:
    print('\nRealizando sua conta abaixo. Confira o resultado:')
    
    if operadores == "+":
        resultado = (numero1 + numero2)  # Removidas as chaves {} de dentro do cálculo
        print(f"{numero1} + {numero2} = {resultado}")
        
    elif operadores == "-":
        resultado = (numero1 - numero2)
        print(f"{numero1} - {numero2} = {resultado}") # Corrigido o sinal e adicionado o resultado
        
    elif operadores == "*":
        resultado = (numero1 * numero2)
        print(f"{numero1} * {numero2} = {resultado}")
    
    # Aqui eu estou me precavendo contra divisões por zero:
    elif operadores == "/":
        if numero2 == 0:
            print("Erro: Não é possível dividir por zero!")
        else:
            resultado = (numero1 / numero2)
            print(f"{numero1} / {numero2} = {resultado}") # Adicionado o resultado no print
    
    print("-" * 30)

    # Corrigido para input() e corrigido a grafia de 'startswith'
    sair = input("Você deseja sair? [s]im: ").lower().startswith("s")
    if sair:
        print("Calculadora encerrada. Até a próxima!")
        break
    