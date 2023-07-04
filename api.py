from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from tensorflow.keras.preprocessing.sequence import pad_sequences
from utils import *

app = FastAPI()


@app.get("/", 
         response_class=HTMLResponse)
def home():
    return '''
    <html>
        <head>
            <title>Clasificador de textos con NLP</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    padding: 20px;
                }
                h1 {
                    color: #333;
                    text-align: center;
                }
                p {
                    color: #666;
                    text-align: center;
                    font-size: 18px;
                    margin-top: 20px;
                }
            </style>
        </head>
        <body>
            <h1>Clasificador de textos con NLP con TensorFlow y predicción en FastAPI</h1>
            <p>Bienvenido a la interfaz del clasificador de textos. ¡Ingresa tu texto y obtén una predicción!</p>
        </body>
    </html>
    '''

# Ruta de la API para la clasificación de texto
@app.post('/clasificar_texto')
async def clasificar_texto(texto: str):
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
