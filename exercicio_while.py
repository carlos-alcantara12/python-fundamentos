
contador = 0
numero = int(input("Digite um valor: "))

while contador < numero:
    contador = contador + numero
    numero = int(input("Digite um valor: "))

print(f"Contador final: {contador}")