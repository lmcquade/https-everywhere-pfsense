import sys
import os
import stat
import json

sys.path.insert(1, os.path.join(os.path.dirname(__file__), "https-everywhere-py"))
from https_everywhere._rules import https_url_rewrite, _reduce_rules

default_rulesets = None
default_rulesets_file = os.path.join(os.path.dirname(__file__), "https-everywhere", "rules", "default.rulesets")
default_rulesets_time = os.stat(default_rulesets_file)[stat.ST_MTIME] - 1

def get_default_rulesets():
    global default_rulesets
    global default_rulesets_time

    new_default_rulesets_time = os.stat(default_rulesets_file)[stat.ST_MTIME]

    if default_rulesets_time != new_default_rulesets_time:
        default_rulesets_time = new_default_rulesets_time

        with open(default_rulesets_file) as f:
            default_rulesets = _reduce_rules(json.load(f), check=False, simplify=False)

    return default_rulesets

while True:
    oldurl = sys.stdin.readline().strip().split(' ')[0]
    redirect = ""

    if oldurl.startswith("http://"):
        if "/" not in oldurl[7:]:
            oldurl += "/"

        newurl = https_url_rewrite(oldurl, get_default_rulesets())

        if newurl != oldurl:
            redirect = "301:" + newurl

    sys.stdout.write(redirect + "\n")
    sys.stdout.flush()
