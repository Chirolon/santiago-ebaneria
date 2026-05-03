import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Ebanistería Santiago", page_icon="🪑")

# Diseño estético con CSS para darle un toque de carpintería (colores madera)
st.markdown("""
    <style>
    .main { background-color: #fdfaf5; }
    h1, h2, h3 { color: #4e342e; }
    .stButton>button { 
        background-color: #795548; 
        color: white; 
        border-radius: 10px;
        width: 100%;
        height: 3em;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Encabezado Principal
st.title("🪑 Ebanistería y Carpintería Santiago")
st.write("### Calidad artesanal y restauración en el corazón de Caballito")

# Imagen de portada profesional
st.image("https://images.unsplash.com/photo-1581429034113-979b907f0b0c?q=80&w=1000&auto=format&fit=crop", 
         caption="Transformamos madera noble en piezas únicas con precisión artesanal.")

st.divider()

# Sección: Galería de Trabajos
st.header("📸 Galería de Trabajos")
st.write("Especialistas en muebles a medida, restauraciones y lustres.")

col1, col2 = st.columns(2)

with col1:
    st.image("https://images.unsplash.com/photo-1594026112284-02bb6f3352fe?q=80&w=500", caption="Muebles a medida")
    st.image("https://images.unsplash.com/photo-1503174971373-b1f69850bded?q=80&w=500", caption="Restauraciones")

with col2:
    st.image("https://images.unsplash.com/photo-1533090161767-e6ffed986c88?q=80&w=500", caption="Terminaciones finas")
    st.image("https://images.unsplash.com/photo-1611269154421-4e27233ac5c7?q=80&w=500", caption="Diseños exclusivos")

st.divider()

# Sección: Servicios y Contacto
st.header("📩 Pedí tu presupuesto")
st.write("Atención personalizada para particulares y empresas. Mandanos tu consulta ahora mismo.")

# Lógica del botón de WhatsApp con el número que pasaste
# Formato internacional: 54 (Argentina) + 9 (Celular) + 11 (CABA) + número sin el 15
celular_santiago = "5491166903089" 
mensaje_predeterminado = "Hola Santiago, vi tu página web y quiero consultarte por un presupuesto."
wa_link = f"https://wa.me/{celular_santiago}?text={mensaje_predeterminado.replace(' ', '%20')}"

st.link_button("Solicitar Presupuesto por WhatsApp ✅", wa_link)

st.info("📍 Ubicación: Av. Acoyte, Caballito, CABA.")