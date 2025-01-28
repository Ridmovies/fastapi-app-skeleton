FROM python:3.12

RUN mkdir /code

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

# Предоставляем права на выполнение скрипту celery.sh
# RUN chmod +x /booking/docker/celery.sh
# RUN chmod +x /booking/docker/app.sh

#CMD ["gunicorn", "src/main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]

# CMD ["fastapi", "run", "src/main.py", "--port", "8000"]
