FROM python:3.6-slim

RUN pip install Flask

COPY . /app

WORKDIR /app

CMD ["python", "./app.py"]