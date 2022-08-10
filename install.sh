#! /usr/bin/env sh

if [ ! -d "/usr/local/libexec/squid/https-everywhere-pfsense" ]; then
    exit 1
fi

cd /usr/local/libexec/squid/https-everywhere-pfsense

pkg install git python39 py39-pip

git clone "https://github.com/EFForg/https-everywhere"
git clone "https://github.com/jayvdb/https-everywhere-py"

/usr/local/bin/pip-3.9 install cached_property logging-helper urllib3 appdirs requests

./update.sh
