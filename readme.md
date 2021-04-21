## Install files to /usr/local/libexec/squid/https-everywhere-pfsense 
```sh
sudo tcsh
cd /usr/local/libexec/squid
pkg install git
git clone "https://github.com/lmcquade/https-everywhere-pfsense"
cd https-everywhere-pfsense
chmod a+x install.sh update.sh
./install.sh
```

## Add Squid Custom Options (before Auth)
```sh
redirect_program /usr/local/bin/python3.7 /usr/local/libexec/squid/https-everywhere-pfsense/squid.py
url_rewrite_children 16
```

## Add Cron entry to update database periodically
```sh
/usr/local/libexec/squid/https-everywhere-pfsense/update.sh
```
