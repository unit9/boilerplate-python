from unit9/base:latest
maintainer Kamil Cholewiński <kamil.cholewinski@unit9.com>

# Dependencies
run apt-get update && \
    apt-get install --yes --no-install-recommends \
            python-pip \
            python-wheel \
            uwsgi-plugin-python \
    && rm -rf /var/cache/apt

# Install app requirements
workdir /app
add requirements.txt /app
run pip install -r ./requirements.txt

# Configure and expose uWSGI
run adduser --system --no-create-home --disabled-login --group app
add config/run_production /etc/service/backend/run

# Slurp application code
add . /app
