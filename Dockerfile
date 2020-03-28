FROM python:3.7-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requeriments.txt /requeriments.txt
RUN pip install -r /requeriments.txt

RUN mkdir /app
WORKDIR /app
COPY ./website /app

RUN adduser -D user
USER user
