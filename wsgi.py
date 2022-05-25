from server import app

import multiprocessing

bind = "0.0.0.0:5000"
workers = multiprocessing.cpu_count() * 2 + 1
threads = multiprocessing.cpu_count() * 2

# pidfile = '/var/run/gunicorn/mysite.pid' # create a simple pid file for gunicorn. 

# user = 'user'          # the user gunicorn will run on

# daemon = True          # this is only to tell gunicorn to deamonize the server process

# errorlog = '/var/log/gunicorn/error-mysite.log'    # error log

# accesslog = '/var/log/gunicorn/access-mysite.log'  # access log

# proc_name = 'gunicorn-mysite'            # the gunicorn process name