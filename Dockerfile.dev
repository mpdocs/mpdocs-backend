FROM python:3.12-alpine

WORKDIR /service

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install poetry==1.7.1

COPY poetry.lock pyproject.toml /service/

RUN poetry install

COPY . /service
