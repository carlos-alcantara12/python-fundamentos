"""Uso de enumerate para obter índice e valor de um iterável."""

nomes = ["Maria", "Helena", "Luiz"]
nomes.append("João")

for indice, nome in enumerate(nomes):
    print(indice, nome)

print("--- Tuplas geradas por enumerate ---")

for item in enumerate(nomes):
    print(item)
