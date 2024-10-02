FROM python:3.12-slim-buster

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

CMD ["streamlit", "run", "app.py"]

