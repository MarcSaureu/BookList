FROM python:3.6-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/

RUN apk update

RUN pip install -r requirements.txt

COPY . /app

RUN adduser -D runner
USER runner
