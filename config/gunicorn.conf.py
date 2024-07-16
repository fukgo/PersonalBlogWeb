bind = '192.18.0.11:8080'  # 绑定的IP地址和端口
#Gunicorn 将在本地 IP 地址（127.0.0.1）的 8080 端口上监听请求。 bind 设置和 Nginx 的 proxy_pass 设置应该匹配
workers = 4  # 工作进程数
errorlog = '/code/logs/gunicorn/error.log'  # 错误日志文件的路径
accesslog = '/code/logs/gunicorn/access.log'  # 访问日志文件的路径
loglevel = 'debug'  # 日志级别
wsgi_app = 'django_web.wsgi:application'

