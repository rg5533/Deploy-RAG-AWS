FROM python:3.11-slim-bullseye

WORKDIR /app

COPY . /app/

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Install requirements with more flexibility
RUN pip install --no-cache-dir -r requirements.txt --use-pep517

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]

