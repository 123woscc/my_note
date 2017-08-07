# uWsgi的配置

1.安装

```
pip install uwsgi
```

2.命令行启动

```
uwsgi --socket 127.0.0.1:3031 --wsgi-file myflaskapp.py --callable app --processes 4 --threads 2 --stats 127.0.0.1:9191
```

3.文件配置启动

```
[uwsgi]
http = :9090
chdir = path_to_app
module = wsgi:app
master = true
processes = 8
```

> 如果出现 `invalid request block size: 21573 (max 4096)...skip`这个错误，请将配置中的 `socket` 改为 `http`，具体可以参考[这里](http://stackoverflow.com/questions/15878176/uwsgi-invalid-request-block-size)。

我的配置

```
[uwsgi]
http = :5000
chdir = /path/to/app
#虚拟环境
venv=/path/to/venv
processes = 4
#文件
wsgi-file=app.py
#application
callable=app
threads = 2
master = true
buffer-sizw=32768
```



