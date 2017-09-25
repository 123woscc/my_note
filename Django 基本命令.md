# Django 基本命令

### 1.新建项目

```
django-admin.py startproject [name]
```

### 2.新建app

```
Python3 manage.py startapp [name]
或者
django-admin.py startapp [name]
```

### 3.同步数据库

```
python manage.py makemigrations
python manage.py migrate
```

### 4.使用开发服务器

```
python manae.py runserver
```

### 5.清空数据库

```
python manage.py flush
```

### 6.创建超级管理员

```
python manage.py createsuperuser
#修改密码
python managr.py changepassword username
```

### 7.导出数据 导入数据

```
python manage.py dumpdata appname > appname.json
python maange.py laoddata appname.json
```

### 8.Django项目环境终端

```
python manage.py shell
```

### 9.数据命令行

```
python manage.py dbshell
```



