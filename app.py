import streamlit as st

# Configuração da página web
st.set_page_config(page_title="Calculadora Segura", page_icon="🧮", layout="centered")

st.title("=== CALCULADORA WEB ===")
st.write("Desenvolvida por Carlos - Foco em Validação Segura de Dados")
st.markdown("---")

# Criando o formulário na web
with st.form(key="calculadora_form"):
    
    # Entradas de dados (o Streamlit já nos dá campos limpos)
    numero1_input = st.text_input("Digite o primeiro valor:")
    numero2_input = st.text_input("Digite o segundo valor:")
    
    # Caixa de seleção para o operador
    operador = st.selectbox("Selecione o operador:", ["+", "-", "*", "/"])
    
    # Botão para enviar o formulário e calcular
    botao_calcular = st.form_submit_button(label="Calcular")

# Se o usuário clicar no botão, processamos os dados com a sua lógica de segurança
if botao_calcular:
    
    # --- Validação de Entrada (Sua lógica de Try/Except!) ---
    try:
        # Tentamos converter as entradas de texto para float
        numero1 = float(numero1_input)
        numero2 = float(numero2_input)
        numeros_validos = True
    except ValueError:
        numeros_validos = False

    # Se a validação falhar, barramos a execução (Sanitização de Input)
    if not numeros_validos:
        st.error("Erro: Um ou ambos os valores fornecidos não são números válidos. Entrada bloqueada!")
    
    else:
        # --- Execução dos Cálculos ---
        st.info("Realizando sua conta de forma segura. Confira o resultado abaixo:")
        
        if operador == "+":
            resultado = numero1 + numero2
            st.success(f"Resultado: {numero1} + {numero2} = **{resultado}**")
            
        elif operador == "-":
            resultado = numero1 - numero2
            st.success(f"Resultado: {numero1} - {numero2} = **{resultado}**")
            
        elif operador == "*":
            resultado = numero1 * numero2
            st.success(f"Resultado: {numero1} * {numero2} = **{resultado}**")
            
        elif operador == "/":
            # Proteção contra Divisão por Zero
            if numero2 == 0:
                st.error("Erro de Segurança: Não é possível dividir por zero!")
            else:
                resultado = numero1 / numero2
                st.success(f"Resultado: {numero1} / {numero2} = **{resultado}**")