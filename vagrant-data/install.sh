#!/bin/bash

# Script to set up a Django project on Vagrant.

set -e # Exit script immediately on first error.

if [ -f /home/vagrant/.provisioned ]; then
    echo "This box has already been provisioned."
    exit 0
fi

# Installation settings

PROJECT_NAME='utdallasiia_site'
PROJECT_DIR=/vagrant

VIRTUALENV_NAME=$PROJECT_NAME
VIRTUALENV_DIR=/home/vagrant/.virtualenvs/$PROJECT_NAME

DB_NAME=$PROJECT_NAME
PGSQL_VERSION=9.1

# Need to fix locale so that Postgres creates databases in UTF-8
cat << EOF >> /etc/bash.bashrc
export LANGUAGE=en_US.UTF-8
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
EOF

locale-gen en_US.UTF-8
dpkg-reconfigure locales

export LANGUAGE=en_US.UTF-8
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8

# Install essential packages from Apt
apt-get update -y
# Python dev packages
apt-get install -y python-dev virtualenvwrapper
# Postgresql
apt-get install -y postgresql-$PGSQL_VERSION libpq-dev
# Dependencies for image processing with PIL
apt-get install -y libjpeg62-dev zlib1g-dev libfreetype6-dev liblcms1-dev
# Others
apt-get install -y vim git

# postgresql global setup
cp $PROJECT_DIR/vagrant-data/pg_hba.conf /etc/postgresql/$PGSQL_VERSION/main/
/etc/init.d/postgresql reload

# postgresql setup for project
createdb -Upostgres $DB_NAME

# virtualenv setup for project
su - vagrant -c "source /etc/bash_completion.d/virtualenvwrapper && \
    mkvirtualenv -a $PROJECT_DIR -r $PROJECT_DIR/requirements/local.txt $VIRTUALENV_NAME"

echo "workon $VIRTUALENV_NAME" >> /home/vagrant/.bashrc

# Provisioned
touch /home/vagrant/.provisioned
