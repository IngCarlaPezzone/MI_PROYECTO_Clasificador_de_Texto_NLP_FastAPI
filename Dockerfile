FROM python:3.10-slim

WORKDIR /st_app

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

RUN python3 -m nltk.downloader -d /usr/local/lib/python3.10/site-packages/nltk/corpus stopwords

EXPOSE 8501

COPY . .

ENTRYPOINT ["streamlit", "run"]

CMD ["st_app.py"]