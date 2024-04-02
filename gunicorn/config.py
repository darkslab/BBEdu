"""Gunicorn *development* config file"""

import multiprocessing

# Django WSGI application path in pattern MODULE_NAME:VARIABLE_NAME
wsgi_app = "bbedu.wsgi"
# The granularity of Error log outputs
loglevel = "debug"
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

 
user = "razrab1"
group = "nginx"
# preload_app = True

pythonpath = "/home/razrab1/BBEdu"

# sudo systemctl daemon-reload && sudo systemctl restart gunicorn && sleep 1 && sudo systemctl status gunicorn
# ExecStart=/usr/local/bin/gunicorn -c /home/dd/BBEdu/gunicorn/conf.py