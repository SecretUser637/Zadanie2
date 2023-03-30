FROM python:3.11

WORKDIR /app

RUN pip install "fastapi[all]"

COPY . /app