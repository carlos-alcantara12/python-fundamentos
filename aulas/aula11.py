# Operadores (in) e (not in)

nome = "CARLOS"
print('C' in nome)
print('z' in nome)
print("CAR" in nome)
print("LOS" not in nome)

nome = input('Digite o nome:')
encontrar = input("O que deseja encontrar?")

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f"{encontrar} não está em {nome}")