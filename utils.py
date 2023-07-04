# Importaciones necesarias
import tensorflow as tf
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences
import json

import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.stem import WordNetLemmatizer

# Seteo de la longitud máxima para la secuencia
longitud_maxima_de_secuencia = 500

# Categorías de los temas a predecir
categorias = ['Meteorology', 'Biology', 'Sport']

# Carga los pesos del modelo y el tokenizer
model = tf.keras.models.load_model('modelo/pesos_modelo.h5')

# Cargar el tokenizer desde un archivo JSON
def load_tokenizer_from_json(json_file):
    '''
    Carga el json con los datos del tokenizer entrenado
    '''
    with open(json_file, 'r') as f:
        tokenizer_data = json.load(f)
        tokenizer = tokenizer_from_json(tokenizer_data)
    return tokenizer

# Cargar el tokenizer desde el archivo JSON
tokenizer = load_tokenizer_from_json('modelo/tokenizer.json')


def preprocesar_textos(text):
    '''
    Realiza el acondicionamiento de textos para poder hacer predicciones sobre ellos usando el modelo entrenado previamente
    '''
    # Convertir todo a minúsculas
    text = text.lower()

    # Eliminar stopwords, números y signos de puntuación
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    text = ' '.join([lemmatizer.lemmatize(word) for word in text.split() if word not in stop_words and not word.isnumeric()])

    return text

def clasificar_texto(texto: str):
    # Preprocesar el nuevo texto
    preprocessed_text = preprocesar_textos(texto)

    # Tokenizar y secuenciar el texto
    secuencia = tokenizer.texts_to_sequences([preprocessed_text])
    secuencia = pad_sequences(secuencia, 
                              maxlen=longitud_maxima_de_secuencia, 
                              padding='post',
                              truncating='post')

    # Realizar la clasificación del texto
    prediccion = model.predict(secuencia)[0]
    print('prediccion', prediccion)
    predicted_label = categorias[prediccion.argmax()]
    print('--->', predicted_label)
   

