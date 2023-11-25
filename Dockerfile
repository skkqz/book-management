FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=config.settings

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
