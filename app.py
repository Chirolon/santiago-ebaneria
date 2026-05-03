import streamlit as st

# 1. Configuración de página
st.set_page_config(page_title="Ebanistería Santiago | Caballito", page_icon="🪵", layout="wide")

# 2. Diseño de Marca (CSS Inyectado)
st.markdown("""
    <style>
    /* Importar Fuentes Elegantes */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Lato:wght@300;400&display=swap');

    /* Fondo y Color General */
    .main {
        background-color: #fdfaf5;
        color: #3e2723;
        font-family: 'Lato', sans-serif;
    }

    /* Títulos con Serifa */
    h1, h2, h3 {
        font-family: 'Playfair Display', serif !important;
        color: #5d4037 !important;
        text-align: center;
    }

    /* Imágenes con estilo 'Card' */
    img {
        border-radius: 12px;
        transition: transform .3s ease;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }
    img:hover {
        transform: scale(1.03);
    }

    /* EL BOTÓN GIGANTE Y CENTRADO */
    div.stButton > button {
        background-color: #5d4037 !important;
        color: #ffffff !important;
        border-radius: 50px !important;
        border: none !important;
        height: 4em !important;
        font-size: 22px !important;
        font-weight: bold !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        width: 100%;
        box-shadow: 0 6px 20px rgba(93, 64, 55, 0.3);
        transition: all 0.3s ease;
        margin-top: 20px;
    }
    
    div.stButton > button:hover {
        background-color: #795548 !important;
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(93, 64, 55, 0.4);
    }

    .footer-text {
        text-align: center;
        color: #8d6e63;
        font-size: 1em;
        margin-top: 40px;
        padding-bottom: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Encabezado de la Web
st.markdown("<h1 style='font-size: 3.8em; margin-bottom: 0;'>EBANISTERÍA SANTIAGO</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.3em; color: #8d6e63; font-style: italic;'>Tradición, Diseño a Medida y Restauración</p>", unsafe_allow_html=True)

st.markdown("---")

# Imagen Principal (Hero Image)
st.image("https://images.unsplash.com/photo-1581429034113-979b907f0b0c?q=80&w=1200", 
         caption="Artesanía pura desde el corazón de Caballito.")

st.markdown("<br>", unsafe_allow_html=True)

# 4. Galería de Trabajos (Portfolio)
st.header("Nuestro Trabajo")
st.markdown("<p style='text-align: center; font-size: 1.1em;'>Especialistas en transformar maderas nobles en piezas de colección.</p>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.image("https://images.unsplash.com/photo-1594026112284-02bb6f3352fe?q=80&w=600")
    st.markdown("<p style='text-align: center; font-style: italic; margin-top: -10px;'>Muebles de Autor</p>", unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1503174971373-b1f69850bded?q=80&w=600")
    st.markdown("<p style='text-align: center; font-style: italic; margin-top: -10px;'>Restauraciones Históricas</p>", unsafe_allow_html=True)

with col2:
    st.image("https://images.unsplash.com/photo-1533090161767-e6ffed986c88?q=80&w=600")
    st.markdown("<p style='text-align: center; font-style: italic; margin-top: -10px;'>Interiores de Lujo</p>", unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1611269154421-4e27233ac5c7?q=80&w=600")
    st.markdown("<p style='text-align: center; font-style: italic; margin-top: -10px;'>Acabados Artesanales</p>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()

# 5. Sección de Cierre y Botón de Acción
st.header("Iniciemos tu proyecto")
st.markdown("<p style='text-align: center; font-size: 1.2em;'>Presupuestos sin cargo para muebles nuevos o restauraciones.</p>", unsafe_allow_html=True)

# Configuración del WhatsApp de Santiago
celular_santiago = "5491166903089" 
mensaje_texto = "Hola Santiago, vi tu catálogo online y quería consultarte por un trabajo de carpintería."
wa_link = f"https://wa.me/{celular_santiago}?text={mensaje_texto.replace(' ', '%20')}"

# Centrado del botón gigante usando columnas
izq, centro, der = st.columns([1, 5, 1])

with centro:
    st.link_button("Solicitar Presupuesto vía WhatsApp ✅", wa_link)

# Footer con ubicación
st.markdown(f"""
    <div class='footer-text'>
        <br>
        <strong>📍 Av. Acoyte, Caballito, Ciudad de Buenos Aires</strong> <br>
        Atención personalizada de Lunes a Viernes.
    </div>
    """, unsafe_allow_html=True)