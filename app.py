import streamlit as st
import random
import string

# Configuração da página
st.set_page_config(page_title="Gerador de Senhas", page_icon="🔐")

st.title("🔐 Gerador de Senhas Seguras")
st.write("Configure os parâmetros abaixo para gerar uma senha forte.")

# Sliders e Checkboxes para customização
tamanho = st.slider("Comprimento da senha", min_value=6, max_value=32, value=12)

col1, col2 = st.columns(2)
with col1:
    usar_maiusculas = st.checkbox("Letras Maiúsculas", value=True)
    usar_numeros = st.checkbox("Números", value=True)
with col2:
    usar_minusculas = st.checkbox("Letras Minúsculas", value=True)
    usar_especiais = st.checkbox("Símbolos", value=True)

def gerar_senha(tamanho, maius, minus, num, espec):
    caracteres = ""
    if maius: caracteres += string.ascii_uppercase
    if minus: caracteres += string.ascii_lowercase
    if num: caracteres += string.digits
    if espec: caracteres += string.punctuation
    
    if not caracteres:
        return "Selecione pelo menos uma opção!"
    
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

# Botão para gerar
if st.button("Gerar Senha"):
    senha = gerar_senha(tamanho, usar_maiusculas, usar_minusculas, usar_numeros, usar_especiais)
    st.success(f"Sua senha gerada:")
    st.code(senha, language="text")
