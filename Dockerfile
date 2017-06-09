FROM unit9/base:latest
MAINTAINER ChangeMe <change.me@example.com>

# Dependencies
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive \
    apt-get install --yes --no-install-recommends \
        python-pip \
        python-wheel \
        uwsgi-plugin-python \
    && rm -rf /var/cache/apt

# Install app requirements
WORKDIR /app
ADD requirements.txt /app
RUN pip install -r ./requirements.txt

# Configure and expose uWSGI
RUN adduser --system --no-create-home --disabled-login --group app
ADD config/run_production /etc/service/backend/run

# Slurp application code
ADD . /app
