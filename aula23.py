lista = ["Carlos", "Joao", "Gabriel", "Julia"]
lista.append("Bernardo")

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))

