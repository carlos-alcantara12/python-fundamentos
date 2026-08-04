nome = 'Carlos Eduardo'
altura = 1.76
peso = 83

# CORRIGIDO: '//' (divisão inteira) truncava o resultado do IMC,
# que precisa de casas decimais para ser preciso.
imc = peso / altura**2

print("Seu nome é", nome)
print(nome, "possui", altura, 'de altura')
print("Ele pesa", peso)

# CORRIGIDO: o print final não imprimia a variável 'imc', só o texto fixo.
print(f'E seu IMC é {imc:.2f}')
