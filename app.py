import streamlit as st

# 1. Configuración de página
st.set_page_config(page_title="Ebanistería Santiago | Caballito", page_icon="🪵", layout="wide")

# 2. Inyección de CSS Avanzado para diseño Pro
st.markdown("""
    <style>
    /* Importar Fuentes de Google */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Lato:wght@300;400&display=swap');

    /* Fondo y texto general */
    .main {
        background-color: #fdfaf5;
        color: #3e2723;
        font-family: 'Lato', sans-serif;
    }

    /* Títulos elegantes */
    h1, h2, h3 {
        font-family: 'Playfair Display', serif !important;
        color: #5d4037 !important;
        text-align: center;
    }

    /* Estilo para las imágenes (Tarjetas con sombra) */
    img {
        border-radius: 15px;
        transition: transform .2s;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    img:hover {
        transform: scale(1.02);
    }

    /* Botón de WhatsApp Premium */
    .stButton>button {
        background-color: #5d4037 !important;
        color: #ffffff !important;
        border-radius: 50px !important;
        border: none !important;
        padding: 15px 30px !important;
        font-weight: bold !important;
        font-size: 20px !important;
        width: 100%;
        box-shadow: 0 4px 15px rgba(93, 64, 55, 0.3);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #795548 !important;
        transform: translateY(-2px);
    }

    /* Footer / Info */
    .footer-text {
        text-align: center;
        color: #8d6e63;
        font-size: 0.9em;
        margin-top: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Contenido de la Landing Page
# Título Hero
st.markdown("<h1 style='font-size: 3.5em; margin-bottom: 0;'>EBANISTERÍA SANTIAGO</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2em; color: #8d6e63;'>Diseño a medida & Restauración artesanal</p>", unsafe_allow_html=True)

st.markdown("---")

# Imagen Principal con ancho completo
st.image("https://images.unsplash.com/photo-1581429034113-979b907f0b0c?q=80&w=1200", 
         caption="Tradición en madera noble desde el corazón de Caballito.")

st.markdown("<br>", unsafe_allow_html=True)

# 4. Galería Estilo "Lookbook"
st.header("Nuestro Portfolio")
col1, col2 = st.columns(2)

with col1:
    st.image("https://images.unsplash.com/photo-1594026112284-02bb6f3352fe?q=80&w=600")
    st.markdown("<p style='text-align: center; font-style: italic;'>Muebles de autor a medida</p>", unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1503174971373-b1f69850bded?q=80&w=600")
    st.markdown("<p style='text-align: center; font-style: italic;'>Restauración de piezas históricas</p>", unsafe_allow_html=True)

with col2:
    st.image("https://images.unsplash.com/photo-1533090161767-e6ffed986c88?q=80&w=600")
    st.markdown("<p style='text-align: center; font-style: italic;'>Interiores en maderas nobles</p>", unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1611269154421-4e27233ac5c7?q=80&w=600")
    st.markdown("<p style='text-align: center; font-style: italic;'>Acabados artesanales</p>", unsafe_allow_html=True)

st.markdown("---")

# 5. Sección de Contacto
st.header("Hablemos de tu proyecto")
st.markdown("<p style='text-align: center;'>Presupuestos personalizados sin cargo. Consultanos por restauración o fabricación desde cero.</p>", unsafe_allow_html=True)

# Botón de WhatsApp con el número real
celular_santiago = "5491166903089" 
mensaje_predeterminado = "Hola Santiago, vi tu catálogo online y quería consultarte por un trabajo de carpintería."
wa_link = f"https://wa.me/{celular_santiago}?text={mensaje_predeterminado.replace(' ', '%20')}"

# Usamos columnas para centrar el botón
left_spacer, center_btn, right_spacer = st.columns([1,2,1])
with center_btn:
    st.link_button("Solicitar Presupuesto vía WhatsApp ✅", wa_link)

# Info de ubicación
st.markdown("""
    <div class='footer-text'>
        📍 Av. Acoyte, Caballito, CABA <br>
        Lunes a Viernes de 9:00 a 18:00hs
    </div>
    """, unsafe_allow_html=True)