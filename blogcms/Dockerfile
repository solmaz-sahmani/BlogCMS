FROM python:3.11-slim

RUN mkdir /app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1 

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt

RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r /app/requirements.txt

COPY . /app/

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]

EXPOSE 8000
