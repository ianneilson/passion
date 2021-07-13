# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Run it
CMD flask run --host=0.0.0.0