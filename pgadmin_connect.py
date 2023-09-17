import streamlit as st
import psycopg2

# Configuración de página
st.set_page_config(
    page_title="Clasificador de textos",
    page_icon="🌈")

# Inicializa la conexión
@st.cache_resource
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

conn = init_connection()

def guardar_prediccion(texto, resultado, probabilidad_formateada):
    cursor = conn.cursor()
    insert_query = "INSERT INTO predicciones (texto, resultado, probabilidad_formateada) VALUES (%s, %s, %s)"
    data = (texto, resultado, probabilidad_formateada)
    cursor.execute(insert_query, data)
    conn.commit()
    cursor.close()
    print("Se guardó correctamente")
    
def guardar_calificacion(texto, calificacion):
    print('Entra a guardar_calificacion')

    cursor = conn.cursor()
    update_query = "UPDATE predicciones SET calificacion = %s WHERE texto = %s"
    data = (calificacion, texto)
    cursor.execute(update_query, data)
    conn.commit()
    cursor.close()
    print("Calificación guardada correctamente.")
