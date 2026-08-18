"""Métodos básicos de listas: append, pop, clear e insert."""

lista = [10, 20, 30]

lista.append(40)
print("Após append:", lista)

item_removido = lista.pop()
print("Após pop:", lista)
print("Item removido:", item_removido)

lista.insert(1, 22)
print("Após insert:", lista)

lista.clear()
print("Após clear:", lista)
