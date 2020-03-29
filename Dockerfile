FROM python:3.7-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY requeriments.txt /app/
RUN pip install -r /requeriments.txt

COPY . /app

RUN adduser -D user
USER user
