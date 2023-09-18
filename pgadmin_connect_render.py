import os
import streamlit as st
import psycopg2

# Se obtiene la URL de la base de datos desde las variables de entorno
DATABASE_URL = os.getenv("DATABASE_URL")

# Inicializa la conexión a la base de datos
@st.cache_resource
def init_connection():
    # Crea una conexión utilizando la URL de la base de datos
    return psycopg2.connect(DATABASE_URL)

# Establece una conexión a la base de datos
conn = init_connection()

def guardar_prediccion(texto, resultado, probabilidad_formateada):
    '''
    Guarda una predicción en la base de datos.

    Parameters:
        texto (str): El texto de la predicción.
        resultado (str): El resultado de la predicción.
        probabilidad_formateada (str): La probabilidad formateada de la predicción.

    Returns:
        None
    '''
    # Abre un cursor para interactuar con la base de datos
    cursor = conn.cursor()
    # Define la consulta de inserción SQL
    insert_query = "INSERT INTO predicciones (texto, resultado, probabilidad_formateada) VALUES (%s, %s, %s)"
    # Crea una tupla con los datos a insertar en la consulta
    data = (texto, resultado, probabilidad_formateada)
    # Ejecuta la consulta de inserción con los datos proporcionados
    cursor.execute(insert_query, data)
    # Confirma los cambios en la base de datos
    conn.commit()
    # Cierra el cursor
    cursor.close()
    
def guardar_calificacion(texto, calificacion):
    '''
    Guarda la calificación asociada a un texto en la base de datos.

    Parameters:
        texto (str): El texto al que se le asignará la calificación.
        calificacion (int): La calificación a asignar al texto.

    Returns:
        None
    '''
    # Abre un cursor para interactuar con la base de datos
    cursor = conn.cursor()
    # Define la consulta de actualización SQL para asignar la calificación
    update_query = "UPDATE predicciones SET calificacion = %s WHERE texto = %s"
    # Crea una tupla con los datos a actualizar en la consulta
    data = (calificacion, texto)
    # Ejecuta la consulta de actualización con los datos proporcionados
    cursor.execute(update_query, data)
    # Confirma los cambios en la base de datos
    conn.commit()
    # Cierra el cursor
    cursor.close()
