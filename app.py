import streamlit as st

# Carregar e aplicar o CSS personalizado
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Título da página
st.title("Preencha seu formulário")

# Criação do formulário
with st.form("form_login"):
    col1, col2, col3 = st.columns([1, 2, 3])

    # Conteúdo do formulário centralizado na coluna 2
    with col2:
        st.markdown("### Painel de Login")
        st.text_input("Email", placeholder="Digite aqui seu Email")
        st.text_input("Senha", placeholder="Digite aqui sua senha", type="password")
        
        # Campo para upload de arquivo
        uploaded_file = st.file_uploader(
            "Escolha um arquivo",
            # type=["png", "jpg", "jpeg", "pdf", "csv", "xlsx"]
        )

        # Botão de submissão do formulário
        submit_button = st.form_submit_button("Login")

    # Verifica se um arquivo foi enviado
    if uploaded_file is not None:
        st.success(f"Arquivo '{uploaded_file.name}' enviado com sucesso!")
        st.write(f"Tamanho do arquivo: {uploaded_file.size} bytes")

# Botão adicional fora do formulário (caso necessário)
st.button("Botão de teste")