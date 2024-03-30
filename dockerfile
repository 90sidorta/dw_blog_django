# Base image
FROM python:3.10-bullseye as development_build

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update && \
    apt-get upgrade -y && \
    pip3 install poetry

# set work directory
WORKDIR /code
COPY pyproject.toml poetry.lock /code/

# Install dependencies:
RUN poetry install
# copy project
COPY . .
