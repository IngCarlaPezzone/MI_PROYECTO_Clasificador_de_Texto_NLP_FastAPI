# Clasificador de textos con NLP con tensorflow y predicción en FastAPI

Este proyecto consiste en la clasificación de textos con un modelo de redes neuronales utilizando LSTM bidireccionales. Para facilitar la interacción con el modelo, se implementó una interfaz usando FastAPI.

Para el entrenamiento se recolectaron 150 URL de wikipedia de tres categorías distintas. Para obtener el listado de las URL se utilizó ChatGPT y con python se automatizó la extracción de los textos, la limpieza y generación del conjunto de datos limpio.

Finalmente, se creó una API donde se puede ingresar un nuevo texto y solicitar la clasificación del mismo.

## Creación del Conjunto de Datos y Entrenamiento del modelo

Se adjunta una Colab (se puede abrir directamente con el botón de Colab) donde explica paso a paso para:
- armar el conjunto de datos, 
- realizar la limpieza de los textos,
- hacer el acondicionamiento para usarlo en el modelo,
- crear y entrenar el modelo,
- evaluar el modelo,
- realizar una predicción.

## Clonar este repositorio
Para realizar la interacción con FastAPI y/o con Streamlit se necesita clonar el repositorio. Para ello, elegir una carpeta donde se quiera guardar el proyecto y abrir una terminal en dicha ubicación.
Hacer `git clone https://github.com/IngCarlaPezzone/MI_PROYECTO_Clasificador_de_Texto_NLP_FastAPI.git` para clonar el proyecto.

## Interacción con la interfaz de FastAPI

En caso de querer interactuar con el modelo desde la interfaz que proporciona FastAPI, se deberán seguir los siguientes pasos:

- Preparación del entorno de trabajo en Visual Studio Code:
    * Crear entorno `Python -m venv env`
    * Ingresar al entorno haciendo `venv\Scripts\activate`
    * Instalar dependencias con `pip install -r requirements.txt`
- Descargar la carpeta modelos que se genera en Colab y que contiene `Pesos_modelo.h5` y `tokenizador.json` y guardarlo en la carpeta de trabajo.
- Ejecutar el archivo api.py desde consola activando uvicorn. Para ello, hacer `uvicorn api:app --reload`
- Hacer Ctrl + clic sobre la dirección `http://127.0.0.1:8000`
- Una vez en el navegador, agregar `/docs` para acceder a ReDoc
- En POST hacer clic en Try it out y luego introducir el texto a clasificar en el campo requerido texto. Finalmente Ejecutar y observar la predicción.

# Actualización!! (18/07/23)

## Interacción con la interfaz de Streamlit

Streamlit es una biblioteca de Python que permite crear aplicaciones web interactivas y visualizaciones de datos de manera rápida y sencilla.

Para poder usarlo, se deberán seguir los siguientes pasos:

- Clonar el repositorio (ver punto anterior)
- Preparación del entorno de trabajo en Visual Studio Code (ver punto anterior)
- Ejecutar `streamlit run st_app.py` desde consola. Se abrirá una nueva pestaña en el navegador.
- Una vez en el navegador, ingresar el nuevo texto y presionar en el botón para obtener la predicción.

Así se ve la interfaz:

![](https://github.com/IngCarlaPezzone/MI_PROYECTO_Clasificador_de_Texto_NLP_FastAPI/blob/main/images/app_streamlit.png)
