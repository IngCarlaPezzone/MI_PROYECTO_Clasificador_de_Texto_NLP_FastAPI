import pymysql

# Establecer la conexión

mydb = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '123456',
    database = 'clasificador_texto',
    charset='utf8mb4'
)

my_cursor = mydb.cursor()
print("Se conectó correctamente")

def guardar_prediccion(texto, resultado, probabilidad_formateada):
    cursor = mydb.cursor()
    insert_query = "INSERT INTO predicciones (texto, resultado, probabilidad_formateada) VALUES (%s, %s, %s)"
    data = (texto, resultado, probabilidad_formateada)
    cursor.execute(insert_query, data)
    mydb.commit()
    cursor.close()
    print("Se guardó correctamente")
    
def guardar_calificacion(texto, calificacion):
    print('Entra a guardar_calificacion')
    try:
        cursor = mydb.cursor()
        update_query = "UPDATE predicciones SET calificacion = %s WHERE texto = %s"
        data = (calificacion, texto)
        cursor.execute(update_query, data)
        mydb.commit()
        cursor.close()
        print("Calificación guardada correctamente.")
    except pymysql.connector.Error as error:
        print(f"Error al guardar la calificación: {error}")