FROM unit9/web-py27:latest
MAINTAINER ChangeMe <change.me@example.com>

# Dependencies
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive \
    apt-get install --yes --no-install-recommends \
        build-essential \
        git \
        libffi-dev \
        libyaml-dev \
    && rm -rf /var/cache/apt

# Install app requirements
ADD requirements-lock.txt /app
RUN pip install -r ./requirements-lock.txt \
    && echo "Outdated requirements:" \
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
