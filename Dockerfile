# Use the official Python image as the base image
FROM python:3.11-slim-bookworm

# Set environment variables
ARG YOUR_ENV

ENV YOUR_ENV=${YOUR_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  # Poetry's configuration:
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry' \
  POETRY_HOME='/usr/local' \
  POETRY_VERSION=2.1.2
  # ^^^
  # Make sure to update it!

RUN apt-get update \
  && apt-get install --no-install-recommends -y \
    # deps for installing poetry
    curl

# System deps:
RUN curl -sSL https://install.python-poetry.org | python3 -

# Set the working directory
WORKDIR /code

# Copy the project files
COPY poetry.lock pyproject.toml /code/

# Project initialization:
RUN poetry install $(test "$YOUR_ENV" == production && echo "--only=main") --no-interaction --no-ansi

# Creating folders, and files for a project:
COPY . /code

# Command to run the application
CMD ["waitress-serve", "hello:app"]