FROM python:3.10-slim

WORKDIR /st_app

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

#RUN python3 -m nltk.downloader -d /usr/local/lib/python3.10/site-packages/nltk/corpus stopwords
ENV NLTK_DATA /nltk_data/ ADD . $NLTK_DATA

# RUN python3 -m nltk.downloader stopwords -d /usr/share/nltk_data

RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold" && apt-get install -y python3-pip \
    && pip3 install nltk --no-cache-dir \
    && python3 -m nltk.downloader -d /usr/local/share/nltk_data stopwords wordnet

EXPOSE 8501

COPY . .

ENTRYPOINT ["streamlit", "run"]

CMD ["st_app.py"]