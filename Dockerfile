
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /app

COPY ./app /app
COPY requirements.txt /app

RUN pip install --no-cache-dir -r /app/requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "localhost", "--port", "8000"]
