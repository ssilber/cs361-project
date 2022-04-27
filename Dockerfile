FROM python:3.10-buster

RUN mkdir -p /project
WORKDIR /project

COPY pyproject.toml /project/pyproject.toml
COPY poetry.lock /project/poetry.lock
RUN pip install poetry==1.1.4
RUN poetry config virtualenvs.create false
RUN poetry install --no-root

COPY . /project
