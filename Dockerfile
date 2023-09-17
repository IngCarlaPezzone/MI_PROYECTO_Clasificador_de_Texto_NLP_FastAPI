# Imagen
FROM python:3.10-slim

# directorio de trabajo de la app
WORKDIR /st_app

# Crea el directorio .streamlit
RUN mkdir -p /app/.streamlit

# Copia el archivo secrets.toml desde /etc/secrets/ a .streamlit/
COPY /etc/secrets/secrets.toml /app/.streamlit/secrets.toml

# Copia los requerimientos del anfitrion
COPY requirements.txt ./requirements.txt

# Instala los requerimientos
RUN pip install -r requirements.txt

# Crea una variable para guardar los descargables de nltk
ENV NLTK_DATA /nltk_data/ ADD . $NLTK_DATA

# Descarga y guarda stopwords y wordnet
RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold" && apt-get install -y python3-pip \
    && pip3 install nltk --no-cache-dir \
    && python3 -m nltk.downloader -d /usr/local/share/nltk_data stopwords wordnet

# Puerto
EXPOSE 8501

# Copia todo lo del anfitrion (clonado de github)
COPY . .

# Comando que se ejecutarán cuando inicie el contenedor
ENTRYPOINT ["streamlit", "run"]

# Argumentos para el comando entrypoint
CMD ["st_app.py"]