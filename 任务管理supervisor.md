# 进程管理supervisor

1.安装

```
apt-get install supervisor
```

2.创建进程文件

```
cd /etc/supervisor/conf.d
touch app.conf
vim app.conf
```

3.编写文件内容

```
#进程名称
[program:ipgeter]
#进程命令
command=/home/ming/ip_geter/venv/bin/uwsgi /home/ming/ip_geter/config.ini
#进程的当前目录
directory=/home/ming/ip_geter
#进程用户身份
user=root
#自动开启和重启
autostart=true
autorestart=true
#超时和重试
startsecs =20
startretries =3
#进程的日志文件
stdout_logfile=/home/ming/uwsgi_supervisor.log
#更多配置http://supervisord.org/configuration.html
```

4.开启

```
#先重启让配置文件生效
service supervisor restart
#开启进程
supervisorctl start app
#停止进程
supervisorctl stop app
#进程状态
supervisorctl status
```

