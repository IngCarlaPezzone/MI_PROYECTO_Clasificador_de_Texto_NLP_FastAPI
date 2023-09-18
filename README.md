![Python](https://img.shields.io/badge/-Python-333333?style=flat&logo=python)
![TensorFlow](https://img.shields.io/badge/-TensorFlow-333333?style=flat&logo=tensorflow)
![Pandas](https://img.shields.io/badge/-Pandas-333333?style=flat&logo=pandas)
![Numpy](https://img.shields.io/badge/-Numpy-333333?style=flat&logo=numpy)
![Scikitlearn](https://img.shields.io/badge/-Scikitlearn-333333?style=flat&logo=scikitlearn)
![Matplotlib](https://img.shields.io/badge/-Matplotlib-333333?style=flat&logo=Matplotlib)
![FastAPI](https://img.shields.io/badge/-FastAPI-333333?style=flat&logo=fastapi)
![Streamlit](https://img.shields.io/badge/-Streamlit-333333?style=flat&logo=streamlit)
![ChatGPT](https://img.shields.io/badge/-ChatGPT-333333?style=flat&logo=openai)
![Docker](https://img.shields.io/badge/-Docker-333333?style=flat&logo=docker)
![Render](https://img.shields.io/badge/-Render-333333?style=flat&logo=render)
![Postgres](https://img.shields.io/badge/-Postgres-333333?style=flat&logo=postgresql)

# Clasificador de textos con tensorflow y predicción en FastAPI, Streamlit y Deploy en Render

Este proyecto consiste en la clasificación de textos con un modelo de redes neuronales utilizando LSTM bidireccionales. Para facilitar la interacción con el modelo, se implementó una interfaz usando FastAPI. Luego, en las actualizaciones posteriores, se agregó una interfaz de Streamlit y finalmente el deploy en Render.

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
- Hacer Ctrl + clic sobre la dirección `http://XXX.X.X.X:XXXX` (se muestra en la consola).
- Una vez en el navegador, agregar `/docs` para acceder a ReDoc.
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

# Actualización!! (26/08/23)

## Deploy de la app de streamlit en render.com

Se hizo el deploy de la aplicación realizada en streamlit en `render.com` que es una nube unificada para crear y ejecutar aplicaciones y sitios web y despliegues automáticos desde Git. Para poder deployar este proyecto se siguieron estos pasos:

- Generación de un Dockerfile cuya imagen es Python 3.10. Esto se hace porque Render usa por defecto Python 3.7, lo que no es compatible con las versiones de las librerías trabajadas en este proyecto, por tal motivo, se opctó por deployar el proyecto dentro de este contenedor. Por otra parte, también fue necesario agregar en la creación del contenedor la descarga de las stopwords y wordnet de NLTK, dado que en el scrip original del proyecto se hacía mediante descarga y esto no es posible durante el deploy. Se puede ver el detalle del documento [Dockerfile](Dockerfile).
- Se generó un servicio **Web Service** nuevo  en `render.com`, conectado al presente repositorio y utilizando Docker como Runtime.
- Finalmente, el servicio queda corriendo en [https://clasificatexto.onrender.com/](https://clasificatexto.onrender.com/).

# Actualización!! (18/09/23)

## Integración con una base de datos Postgres

Se agregaron nuevas funcionalidades a la aplicación de streamlit para guardar el texto ingresado por el usuario, la predicción del modelo y la calificación de la predicción. En este último punto se agregaron secciones a la aplicación para que el usuario califique la predicción como 👍 o 👎. En caso de que el modelo se haya equivocado, y el usuario califique como negativo, se permite al usuario que indique cuál era la predicción real del texto ingresado. De esta manera, se guardan todos estos datos para evaluar el modelo y para un futuro reentrenamiento del modelo.

Para hacer esta integración con la base de datos se realizaron los siguientes pasos:

- Se modificó el código [st_app.py](st_app.py) para agregar las nuevas funcionalidades.
- Se creo el archivo [pgadmin_connect_render.py](pgadmin_connect_render.py) donde contiene la conexión a la base de datos Postgres que proporciona Render y las funciones que permiten guarda los datos a la base de datos.
- Se agregó un nuevo servicio **PostgreSQL** en `render.com`.
- Se agregó como variable de ambiente la **Internal Database URL** para conectar el proyecto con la base de datos de Render.
- Se creo una base de datos en `pgAdmin` conectada a la **External Database URL** para conectar con la base de datos de Render. Allí se creó una nueva tabla *predicciones* con los *campos id*, *texto*, *resultado*, *probabilidad_formateada* y *calificacion* donde se almacenan los datos generados por la aplicación.
- Finalmente, el servicio queda corriendo en [https://clasificatexto.onrender.com/](https://clasificatexto.onrender.com/). 

A continuación, se muestran algunas imágenes de la aplicación:

### Opciones para calificar la predicción

![](https://github.com/IngCarlaPezzone/MI_PROYECTO_Clasificador_de_Texto_NLP_FastAPI/blob/main/images/opciones_calificacion.png)

### Resultado de predicción positiva

![](https://github.com/IngCarlaPezzone/MI_PROYECTO_Clasificador_de_Texto_NLP_FastAPI/blob/main/images/predicci%C3%B3n_positiva.png)

### Opciones cuando la predicción fue negativa

Aca se muestran las opciones distintas a la que predijo el modelo. Porque si califica la predicción como 👎 quiere decir que esa categoría no era correcta y debe elegir por alguna de las otras dos categorías.

![](https://github.com/IngCarlaPezzone/MI_PROYECTO_Clasificador_de_Texto_NLP_FastAPI/blob/main/images/opciones_negativa.png)
