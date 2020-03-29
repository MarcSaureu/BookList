FROM python:3.7-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /booklist
WORKDIR /booklist

COPY requeriments.txt /booklist/
RUN apk update
RUN pip install -r requeriments.txt

COPY . /booklist

RUN adduser -D user
USER user
