FROM python:3.8

ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV FLASK_APP=src/markov_api/app.py

RUN pip install poetry

WORKDIR /app
COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction
COPY . /app

RUN env FLASK_APP=src/markov_api/app.py flask run

EXPOSE 5000
