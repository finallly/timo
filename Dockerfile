FROM python:3.10.0

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . /app/
WORKDIR /app

RUN pip install -r requirements.txt
RUN python manage.py collectstatic