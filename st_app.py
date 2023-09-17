import streamlit as st

# Configura el título y el icono de la pestaña del navegador.
st.set_page_config(
    page_title="Clasificador de textos",
    page_icon="🌈")

from utils import clasificar_texto
from pgadmin_connect import guardar_prediccion, guardar_calificacion

# Titulo de la app
titulo = st.title('Clasificador de textos')

# Introducción
st.write('Este modelo puede clasificar un texto en tres categorías:')
st.write('🌈 Meteorología')
st.write('⚽️ Deporte')
st.write('🧬 Biología')

# Inicializa la sesión de estado
if 'prediccion_realizada' not in st.session_state:
    st.session_state.prediccion_realizada = False

if 'mostrar_casillas' not in st.session_state:
    st.session_state.mostrar_casillas = False

if 'categoria_correcta' not in st.session_state:
    st.session_state.categoria_correcta = False
    
if 'prediccion' not in st.session_state:
    st.session_state.prediccion = None

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

    probabilidad_formateada = float(probabilidad_formateada.replace('%', ''))
    # Guarda la información en una base de datos
    guardar_prediccion(texto, resultado['categoria'], probabilidad_formateada)
    
    st.session_state.prediccion = resultado['categoria']
    
    # Cambia el estado de la variable a True para indicar que la predicción se ha realizado
    st.session_state.prediccion_realizada = True

if st.session_state.prediccion_realizada:
    st.markdown('#### Califica la predicción:')
        
    # Botón de calificación "👍"
    if st.button('👍'):
        calificacion = 'Correcto'
        guardar_calificacion(texto, calificacion)
        st.success('Gracias por calificar la predicción 🤗')
        st.success('Intenta otra predicción 🤓')
        # Restablece las variables de estado para permitir una nueva predicción
        st.session_state.prediccion_realizada = False
        st.session_state.mostrar_casillas = False
        st.session_state.categoria_correcta = False

    # Botón para mostrar las casillas de verificación
    if st.button('👎'):
        st.session_state.mostrar_casillas = True
        
    # Lista de todas las categorías posibles
    categorias = ["Meteorology", "Sport", "Biology"]

    print("predicion es", st.session_state.prediccion)
    # Filtra las categorías que son diferentes a la predicción del modelo
    categorias_filtradas = [cat for cat in categorias if not cat.startswith(st.session_state.prediccion)]

       
    if st.session_state.mostrar_casillas:
        st.markdown('##### Seleccione cuál era la categoría correcta:')
        
        # Muestra las casillas de verificación solo para las categorías filtradas
        for categoria in categorias_filtradas:
            seleccionada = st.checkbox(categoria)
            if seleccionada:
                st.session_state.categoria_correcta = categoria

        if st.session_state.categoria_correcta:
            guardar_calificacion(texto, st.session_state.categoria_correcta)
            st.success('Gracias por calificar la predicción 🤗')
            st.success('Intenta otra predicción 🤓')
            st.session_state.prediccion_realizada = False
            st.session_state.mostrar_casillas = False
            st.session_state.categoria_correcta = None

with st.sidebar:
    # Agrega el enlace a LinkedIn y github
    st.markdown("Mi contacto en:")
    st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/ingambcarlapezzone/)")
    st.markdown("Mas detalles de este proyecto en:")
    st.markdown("[![Github](https://img.shields.io/badge/GitHub-black?style=flat-square&logo=github)](https://github.com/IngCarlaPezzone/MI_PROYECTO_Clasificador_de_Texto_NLP_FastAPI)")
