import math
import operator

import streamlit as st


OPERACOES = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}


def calcular(numero1: float, numero2: float, operador: str) -> float:
    """Executa a operação escolhida e retorna o resultado.

    Lança ZeroDivisionError se for uma divisão por zero.
    """
    if operador == "/" and numero2 == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return OPERACOES[operador](numero1, numero2)


def numero_valido(valor: float) -> bool:
    """Verifica se o valor é um número finito (rejeita inf e nan)."""
    return math.isfinite(valor)


# --- Interface ---

st.set_page_config(page_title="Calculadora Web", page_icon="🧮", layout="centered")

st.title("Calculadora Web")
st.write("Projeto de estudo com validação de entrada e tratamento de erros.")
st.divider()

with st.form(key="calculadora_form"):
    numero1_input = st.text_input("Digite o primeiro valor:")
    numero2_input = st.text_input("Digite o segundo valor:")
    operador = st.selectbox("Selecione o operador:", list(OPERACOES.keys()))
    botao_calcular = st.form_submit_button(label="Calcular")

if botao_calcular:
    try:
        numero1 = float(numero1_input)
        numero2 = float(numero2_input)

        if not (numero_valido(numero1) and numero_valido(numero2)):
            raise ValueError("Valor não é um número finito.")
    except ValueError:
        st.error("Erro: um ou ambos os valores fornecidos não são números válidos.")
    else:
        st.info("Cálculo realizado. Confira o resultado abaixo:")
        try:
            resultado = calcular(numero1, numero2, operador)
        except ZeroDivisionError as erro:
            st.error(f"Erro: {erro}")
        else:
            st.success(f"Resultado: {numero1} {operador} {numero2} = **{resultado}**")
