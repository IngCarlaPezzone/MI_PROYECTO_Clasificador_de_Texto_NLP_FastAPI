import streamlit as st
from tensorflow.keras.preprocessing.sequence import pad_sequences
from utils import *

def clasificar_texto(texto: str):
    '''
    Preprocesa el nuevo texto ingresado, preparándolo para utilizar el 
    modelo previamente entrenado para hacer la clasificación.
    '''
    # Preprocesar el nuevo texto
    preprocessed_text = preprocesar_textos(texto)

    # Tokenizar y secuenciar el texto
    secuencia = tokenizer.texts_to_sequences([preprocessed_text])
    secuencia = pad_sequences(secuencia, 
                              maxlen=longitud_maxima_de_secuencia, 
                              padding='post')

    # Realizar la clasificación del texto
    prediccion = model.predict(secuencia)[0]
    clase = int(prediccion.argmax())
    probabilidad = float(prediccion[clase])

    # Obtener el nombre de la categoría predicha
    categoria_predicha = categorias[clase]

    # Devolver la clase y la probabilidad de la clasificación
    return {'categoria': categoria_predicha, 'clase': clase, 'probabilidad': float(probabilidad)}

# Titulo de la app
titulo = st.title('Clasificador de textos 🌈⚽️🧬')
# Texto que ingresa el usuario
texto = st.text_input('Ingrese el texto a clasificar aquí: 👇')
# Define una función anónima para envolver la llamada a clasificar_texto
clasificar = lambda: clasificar_texto(texto)
# Botón para hacer la predicción
if st.button('Predecir', on_click=clasificar, disabled=len(texto) == 0):
    # Guarda el resultado
    resultado = clasificar_texto(texto)
    # Formatea el número de la probabilidad
    probabilidad_formateada = "{:.2%}".format(resultado['probabilidad'])
    # Escribe la categoría predicha y la probabilidad de la predicción
    # incluye el formato
    st.write('Categoría predicha:', f"<span style='color:green'><b>{resultado['categoria']}</b></span>", unsafe_allow_html=True)
    st.write('Probabilidad:', f"<span style='color:green'><b>{probabilidad_formateada}</b></span>", unsafe_allow_html=True)

# Agregar el enlace a LinkedIn
st.markdown("🔗¡Conéctate conmigo en [LinkedIn](https://www.linkedin.com/in/ingambcarlapezzone/)!")

