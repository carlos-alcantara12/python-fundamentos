# CORRIGIDO: 'n = print(...)' guardava None em 'n', porque print()
# sempre retorna None. Isso quebrava a linha seguinte com TypeError.
numero = int(input('Digite um número inteiro: '))

if numero % 2 == 0:
    print(f"O número {numero} é PAR")
else:
    print(f"O número {numero} é ÍMPAR")

# -----------------------------------------------------------------

# CORRIGIDO: 'nome = print("Digite seu nome:")' não capturava
# nenhum input, só imprimia o texto e guardava None em 'nome'.
nome = input("Digite seu nome: ")
horas = float(input("Digite o horário: "))

# CORRIGIDO: os dois primeiros 'if' testavam faixas mutuamente
# exclusivas sem usar elif, o que podia imprimir mais de uma
# mensagem por engano.
if horas < 12.0:
    print(f'Bom dia, {nome}')
elif horas <= 17.59:
    print(f"Boa tarde, {nome}")
else:
    print(f"Boa noite, {nome}")

# -----------------------------------------------------------------

# CORRIGIDO: 'nome = int(input(...))' tentava converter um nome
# (texto) para número inteiro, o que quebra com qualquer letra digitada.
nome = input("Digite seu primeiro nome: ")
tamanho_nome = len(nome)

if tamanho_nome <= 4:
    print('Seu nome é curto.')
elif tamanho_nome <= 6:
    print("Seu nome é médio.")
else:
    print('Seu nome é grande.')
