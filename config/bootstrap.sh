#!/bin/bash

# add swap if DNE
# swap is necessary for using Docker
if [ $(sudo swapon -s | wc -l) -eq 1 ]
then
    fallocate -l 2G /swapfile
    chmod 600 /swapfile
    mkswap /swapfile
    swapon /swapfile
fi

# installs the package passed in if it's not installed
install () {
    package=$1
    dpkg-query -l $package &> /dev/null
    if [ $? -ne 0 ]; then
        apt-get -y install $package
    fi
}

apt-get -y update

apt-get install -y  git-core
apt-get install -y  git
apt-get install -y  mongodb
apt-get install -y  python
apt-get install -y  python-dev
apt-get install -y  python-pip
apt-get install -y  python-software-properties
apt-get install -y  vim
apt-get install -y  libncurses5-dev

# install docker
install docker.io
service restart docker.io

install curl
install unzip

apt-get -y update

pip install -r /vagrant/config/requirements.txt
pip install -r /vagrant/config/vagrant_requirements.txt
pip install flake8  # for local testing
gem install sass

mkdir -p /vagrant/log

source /vagrant/config/settings.dev

# TODO: setup database and insert any data that is necessary
# service mongodb start

exit 0
