FROM unit9/web-py34:latest
MAINTAINER ChangeMe <change.me@example.com>

# Dependencies
ADD requirements-lock.txt /app
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive \
    apt-get install --yes --no-install-recommends \
        build-essential \
        git \
        libffi-dev \
        libyaml-dev \
        postgresql-common \
        postgresql-server-dev-all \
    && pip install -r ./requirements-lock.txt \
    && apt-get remove --purge --yes build-essential \
    && apt-get autoremove --yes --purge \
    && rm -rf /var/cache/apt /root/.cache \
    && pip list --outdated --format=columns

# Configure and expose uWSGI
ENV PORT=5000 \
    PYTHON_MODULE=backend \
    PYTHON_CALLABLE=application \
    UWSGI_PROCESSES=2 \
    UWSGI_THREADS=32
EXPOSE 5000

# Slurp application code
ADD . /app
