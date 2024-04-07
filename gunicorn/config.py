"""Gunicorn *development* config file"""

import multiprocessing
from pathlib import Path
from json import load
from re import match

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR_PATH = Path(BASE_DIR).resolve()
try:
    with (BASE_DIR_PATH / "secrets.json").open() as settings_file:
        SECRETS = load(settings_file)
except (OSError, ValueError):
    pass

# Django WSGI application path in pattern MODULE_NAME:VARIABLE_NAME
wsgi_app = "bbedu.wsgi"
# The granularity of Error log outputs
loglevel = "error"
# The number of worker processes for handling requests
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "gevent"
# The socket to bind
# bind = "unix:/var/run/gunicorn.sock"
bind = "0.0.0.0:8001"
# Restart workers when code changes (development only!)
# reload = False
# Write access and error info to /var/log
# Write access and error info to /var/log
accesslog = "/var/log/gunicorn/access.log"
errorlog = "/var/log/gunicorn/error.log"
# Redirect stdout/stderr to log file
capture_output = True
# PID file so you can easily fetch process ID
pidfile = "/var/run/gunicorn/prod.pid"
# Daemonize the Gunicorn process (detach & enter background)
# daemon = True

 
user = SECRETS["GUNICORN_USER"]
group = "nginx"
# preload_app = True

pythonpath = "/home/razrab1/BBEdu"

# sudo systemctl daemon-reload && sudo systemctl restart gunicorn && sleep 1 && sudo systemctl status gunicorn
# ExecStart=/usr/local/bin/gunicorn -c /home/dd/BBEdu/gunicorn/conf.py