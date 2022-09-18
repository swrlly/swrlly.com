workers = 10
bind = "127.0.0.1:8000"
access_log_format = '%({CF-Connecting-IP}i)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
accesslog = "/home/swrlly/swrlly.com/access.log"