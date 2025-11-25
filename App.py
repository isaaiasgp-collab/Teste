import streamlit as st
import pandas as pd
import time
import random

# Configuração da Página
st.set_page_config(
    page_title="Mangaba Trip | Hack.IA++",
    page_icon="🌴",
    layout="centered"
)

# --- MANGABA AI ENGINE (INTEGRAÇÃO) ---
# Simulação da Arquitetura de Agentes (Mangaba Framework v2.0)
class MangabaEngine:
    def __init__(self):
        # Base de Conhecimento (Simulada)
        self.knowledge_base = {
            "natureza": {
                "destino": "Cânion do Xingó",
                "img": "https://visitbrasil.com/wp-content/uploads/2021/06/Canion-do-Xingo-Sergipe.jpg",
                "copy": "Navegue pelas águas do Velho Chico cercado por paredões milenares. A escolha perfeita para seu perfil explorador."
            },
            "praia": {
                "destino": "Croa do Goré",
                "img": "https://www.visitearacaju.com.br/assets/img/galeria/croa-do-gore/01.jpg",
                "copy": "Um banco de areia exclusivo que surge apenas na maré baixa. Gastronomia flutuante e relaxamento total."
            },
            "historia": {
                "destino": "São Cristóvão (Patrimônio da UNESCO)",
                "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Pra%C3%A7a_S%C3%A3o_Francisco_-_S%C3%A3o_Crist%C3%B3v%C3%A3o_-_Sergipe_-_Brasil.jpg/1200px-Pra%C3%A7a_S%C3%A3o_Francisco_-_S%C3%A3o_Crist%C3%B3v%C3%A3o_-_Sergipe_-_Brasil.jpg",
                "copy": "Respire a história na quarta cidade mais antiga do Brasil. Ideal para seu interesse cultural."
            }
        }

    def processar_recomendacao(self, perfil):
        """
        Simula o Agente de Recomendação da Mangaba AI.
        Entrada: Perfil do usuário (User-Based Filtering)
        Saída: Objeto de recomendação enriquecido
        """
        # Lógica de decisão baseada no input
        if "Aventura" in perfil:
            key = "natureza"
        elif "Relax" in perfil:
            key = "praia"
        else:
            key = "historia"
            
        dados = self.knowledge_base[key]
        
        return {
            "destino": dados["destino"],
            "match_score": random.randint(89, 99),
            "imagem": dados["img"],
            "texto_agente": dados["copy"]
        }

# Instancia o Motor
engine = MangabaEngine()

# --- INTERFACE (FRONTEND) ---
# Estilização CSS para Mobile First
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Gerenciamento de Estado (Navegação)
if 'page' not in st.session_state:
    st.session_state.page = 'login'

def navigate_to(page):
    st.session_state.page = page
    st.rerun()

# --- TELA 1: LOGIN ---
if st.session_state.page == 'login':
    st.title("🌴 Mangaba Trip")
    st.caption("Powered by Mangaba.AI Framework")
    st.image("https://images.unsplash.com/photo-1595840636365-5c1798399580?q=80&w=1000")
    
    st.write("### O Co-piloto da sua viagem")
    st.info("Acesse a melhor experiência de turismo em Sergipe.")
    
    with st.form("login_form"):
        st.text_input("Email", placeholder="usuario@email.com")
        st.text_input("Senha", type="password")
        
        if st.form_submit_button("ENTRAR"):
            with st.spinner("Conectando ao Neural Engine..."):
                time.sleep(1.5)
            navigate_to('quiz')

# --- TELA 2: CALIBRAÇÃO (QUIZ) ---
elif st.session_state.page == 'quiz':
    st.title("🎯 Calibrando a IA")
    st.progress(50)
    st.write("Para encontrarmos o match perfeito, conte-nos:")
    
    vibe = st.select_slider("Qual a vibe de hoje?", options=["Relax Total", "História/Cultura", "Aventura Extrema"])
    orcamento = st.select_slider("Orçamento estimado:", options=["Econômico", "Conforto", "Luxo"])
    
    if st.button("GERAR ROTEIRO INTELIGENTE"):
        st.session_state.vibe = vibe
        with st.spinner("Cruzando dados com 5.000 perfis similares..."):
            time.sleep(2)
        navigate_to('dashboard')

# --- TELA 3: RESULTADO (DASHBOARD) ---
elif st.session_state.page == 'dashboard':
    st.success("✨ Destino Encontrado!")
    
    # Chama o Motor
    rec = engine.processar_recomendacao(st.session_state.vibe)
    
    # Exibição
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Índice de Match", f"{rec['match_score']}%")
    with col2:
        st.metric("Custo Médio", "R$ 450,00")
        
    st.header(rec['destino'])
    st.image(rec['imagem'])
    
    st.info(f"🤖 **Mangaba AI diz:**\n\n{rec['texto_agente']}")
    
    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("✅ ACEITAR"):
            st.balloons()
            st.toast("Roteiro enviado para seu email!")
    with col_b:
        if st.button("🔄 REFAZER"):
            navigate_to('quiz')

    st.markdown("---")
    st.caption("Hack.IA++ 2025 | Trilha CustomerTech")
