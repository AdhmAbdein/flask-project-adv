
# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY ./project-code/requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY ./project-code /app

EXPOSE 5000

CMD ["python", "app.py"]
