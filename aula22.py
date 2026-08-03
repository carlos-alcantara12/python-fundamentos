lista1 = [5,6,7]
lista2 = [8,9,10]
lista3 = lista1 + lista2

print(lista3)
lista1.extend(lista2) # O método (extend) é gera uma junçaõ de objetos.
print(lista1)

lista1 = [1,2,3,4]
lista2 = lista1
print(lista2)

lista1 = [2,3,4]
lista2 = lista1.copy()
print(lista2)
