bind = '127.0.0.1:8080'  # 绑定的IP地址和端口
workers = 4  # 工作进程数
#errorlog = '/code/lsogs/gunicorn/error.log'  # 错误日志文件的路径
#accesslog = '/code/logs/gunicorn/access.log'  # 访问日志文件的路径
loglevel = 'debug'  # 日志级别
wsgi_app = 'django_web.wsgi:application'

