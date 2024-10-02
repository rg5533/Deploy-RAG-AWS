FROM python:3.11-slim-bullseye

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

CMD ["streamlit", "run", "app.py"]

