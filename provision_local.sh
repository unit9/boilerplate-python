#!/bin/sh
set -eux

### --> ATTENTION DEVELOPERS <-- ###
# This is where you set up your local provisioning.
# DO:
# - Keep It Simple, Silly
# - Talk to your sysop
# DO NOT:
# - Make this a horrible mess
# - Install 5GB of random crap
# - Make this the only possible way to get your application running
# CONSIDER:
# - This is only to get the app running in your local environment
# - What is necessary to run this in production? You don't run Vagrant on AWS
# - Deployment setup is not your responsibility

id

export DEBIAN_FRONTEND=noninteractive
dpkg --configure -a
apt-get update
apt-get install --yes --no-install-recommends \
        git-core \
        python-pip \
        python-wheel \
        && true

cd /vagrant
git show -s HEAD
git status

pip install -r ./requirements.txt
