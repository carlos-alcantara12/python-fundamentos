"""Concatenação, extend, referência e cópia de listas."""

lista1 = [5, 6, 7]
lista2 = [8, 9, 10]

lista3 = lista1 + lista2
print("Concatenação:", lista3)

lista1.extend(lista2)
print("Após extend:", lista1)

original = [1, 2, 3, 4]
referencia = original
copia = original.copy()

print("Referência:", referencia)
print("Cópia:", copia)
