"""Calculadora de terminal com validação de entrada."""

import math
import operator

OPERACOES = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}

print("=== CALCULADORA ===")

while True:
    try:
        numero1 = float(input("Digite o primeiro valor: "))
        numero2 = float(input("Digite o segundo valor: "))
    except ValueError:
        print("Erro: digite apenas números.")
        continue

    if not (math.isfinite(numero1) and math.isfinite(numero2)):
        print("Erro: use apenas números finitos.")
        continue

    operador = input("Digite um operador (+, -, *, /): ").strip()

    if operador not in OPERACOES:
        print("Erro: operador inválido.")
        continue

    if operador == "/" and numero2 == 0:
        print("Erro: não é possível dividir por zero.")
        continue

    resultado = OPERACOES[operador](numero1, numero2)
    print(f"{numero1} {operador} {numero2} = {resultado}")

    if input("Deseja sair? [S/N]: ").strip().upper() == "S":
        print("Calculadora encerrada.")
        break
