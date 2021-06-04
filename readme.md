
## Enable FreeBSD packages
Set `FreeBSD: { enabled: yes }` in pkg configuration files

```
cd /usr/local/etc/pkg/repos
vi FreeBSD.conf
vi pfSense.conf
pkg update -f

```

## Install files to /usr/local/libexec/squid/https-everywhere-pfsense 
```sh
cd /usr/local/libexec/squid
pkg install git
git clone "https://github.com/lmcquade/https-everywhere-pfsense"
cd https-everywhere-pfsense
chmod a+x install.sh update.sh
./install.sh
```

## Add Squid Custom Options (before Auth)
```sh
redirect_program /usr/local/bin/python3.8 /usr/local/libexec/squid/https-everywhere-pfsense/squid.py
url_rewrite_children 16
```

## Add Cron entry to update database periodically
```sh
/usr/local/libexec/squid/https-everywhere-pfsense/update.sh
```

## Tested with pfSense 21.05