#! /usr/bin/env sh

if [ ! -d "/usr/local/libexec/squid/https-everywhere-pfsense" ]; then
    exit 1
fi

cd /usr/local/libexec/squid/https-everywhere-pfsense

if [ -r "https-everywhere/.git" ]; then
    cd https-everywhere
    git checkout .
    git pull --rebase
    python3.7 utils/merge-rulesets.py
fi
