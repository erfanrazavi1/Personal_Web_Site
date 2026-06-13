FROM python:3.13-slim

RUN mkdir /app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


RUN pip3 install --upgrade pip
# Install gettext for translations
RUN apt-get update && apt-get install -y --no-install-recommends \
    gettext \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt

COPY . /app/