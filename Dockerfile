FROM python:3.9.4-alpine

WORKDIR /app/

COPY . .

RUN pip install -r requirements.txt

RUN python manage.py migrate

EXPOSE 8000

CMD gunicorn product_ms.wsgi:application --bind 0.0.0.0:8000
