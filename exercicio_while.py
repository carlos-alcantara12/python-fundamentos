# CORRIGIDO: 'numero' era usado na condição do while antes de existir,
# causando NameError logo na primeira execução.
contador = 0
numero = int(input("Digite um valor: "))

while contador < numero:
    contador = contador + numero
    numero = int(input("Digite um valor: "))

print(f"Contador final: {contador}")
