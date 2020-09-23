FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN pip install pipenv

RUN apt-get update && apt-get upgrade

ENV PROJECT_DIR /usr/local/src/linkscraping

WORKDIR ${PROJECT_DIR}

COPY Pipfile Pipfile.lock ${PROJECT_DIR}/

RUN pipenv install --system --deploy