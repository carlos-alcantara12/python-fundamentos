
numero = int(input('Digite um número inteiro: '))

if numero % 2 == 0:
    print(f"O número {numero} é PAR")
else:
    print(f"O número {numero} é ÍMPAR")

# -----------------------------------------------------------------


nome = input("Digite seu nome: ")
horas = float(input("Digite o horário: "))


if horas < 12.0:
    print(f'Bom dia, {nome}')
elif horas <= 17.59:
    print(f"Boa tarde, {nome}")
else:
    print(f"Boa noite, {nome}")

# -----------------------------------------------------------------


nome = input("Digite seu primeiro nome: ")
tamanho_nome = len(nome)

if tamanho_nome <= 4:
    print('Seu nome é curto.')
elif tamanho_nome <= 6:
    print("Seu nome é médio.")
else:
    print('Seu nome é grande.') 

