FROM python:3.10-slim

COPY . .

EXPOSE 8501

WORKDIR /st_app

RUN pip install -r requirements.txt

ENTRYPOINT ["streamlit", "run"]

CMD ["st_app.py"]