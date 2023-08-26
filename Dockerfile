FROM python:3.10-slim

WORKDIR /st_app

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

RUN pip install nltk && \
    mkdir ~/nltk_data && \
    python -c "import nltk; nltk.download(['stopwords'])"

EXPOSE 8501

COPY . .

ENTRYPOINT ["streamlit", "run"]

CMD ["st_app.py"]