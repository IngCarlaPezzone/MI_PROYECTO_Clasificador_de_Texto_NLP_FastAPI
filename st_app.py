import streamlit as st
from utils import clasificar_texto

# Configura el título y el icono de la pestaña del navegador
st.set_page_config(
    page_title="Clasificador de textos",
    page_icon="🌈")

# Titulo de la app
titulo = st.title('Clasificador de textos')

# Introducción
st.write('Este modelo puede clasificar un texto en tres categorías:')
st.write('🌈 Meteorología')
st.write('⚽️ Deporte')
st.write('🧬 Biología')

# Texto que ingresa el usuario
texto = st.text_input('Ingrese el texto (en inglés) a clasificar aquí: 👇')

# Define una función anónima para envolver la llamada a clasificar_texto
clasificar = lambda: clasificar_texto(texto)

# Botón para hacer la predicción
if st.button('Predecir', on_click=clasificar, disabled=len(texto) == 0):
    
    # Guarda el resultado
    resultado = clasificar_texto(texto)
    # Formatea el número de la probabilidad
    probabilidad_formateada = "{:.2%}".format(resultado['probabilidad'])
    # Escribe la categoría predicha y la probabilidad de la predicción, incluyendo el formato
    st.write('Categoría predicha:', f"<span style='color:green'><b>{resultado['categoria']}</b></span>", unsafe_allow_html=True)
    st.write('Probabilidad:', f"<span style='color:green'><b>{probabilidad_formateada}</b></span>", unsafe_allow_html=True)

# Agrega el enlace a LinkedIn y github
st.markdown("Mi contacto en: [![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/ingambcarlapezzone/)")
st.markdown("Mas detalles de este proyecto en: [![Github](https://img.shields.io/badge/GitHub-black?style=flat-square&logo=github)](https://github.com/IngCarlaPezzone/MI_PROYECTO_Clasificador_de_Texto_NLP_FastAPI)")
