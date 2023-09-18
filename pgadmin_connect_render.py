import os
import streamlit as st
import psycopg2

# # Inicializa la conexión
# @st.cache_resource
# def init_connection():
#     return psycopg2.connect(**st.secrets["postgres"])
# Obtén las variables de entorno
DATABASE_URL = os.getenv("DATABASE_URL")

# Inicializa la conexión
@st.cache_resource
def init_connection():
    return psycopg2.connect(DATABASE_URL)

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
