FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV POETRY_VIRTUALENVS_CREATE false

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  # Weasy print dependencies
  && apt-get install -y python3-wheel python3-cffi libffi-dev shared-mime-info \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# Install poetry
RUN pip install poetry

# Requirements are installed here to ensure they will be cached.
COPY ./poetry.lock ./pyproject.toml /
  # Install project dependencies
RUN poetry install -n \
  # Clean poetry cache
  && poetry cache clear pypi --all -n

COPY ./backend/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY ./backend/wait_for_pg.sh /wait_for_pg.sh
RUN chmod +x /wait_for_pg.sh

WORKDIR /app

ENTRYPOINT ["/wait_for_pg.sh"]
