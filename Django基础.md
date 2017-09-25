# Django基础

### 1.创建项目

   ```
 django-admin startproject HelloWorld
   ```

### 2.创建APP

```
python3 manage.py startapp Hello
```


### 3.修改views.py文件

```
    from django.shortcuts import render

    from django.http import HttpResponse

    def index(request):

        return HttpResponse(u'Hello World')
```

### 4.添加APP到settings.py文件

  ```
  INSTALLED_APPS = (

    'django.contrib.admin',

    'django.contrib.auth',

    'django.contrib.contenttypes',

    'django.contrib.sessions',

    'django.contrib.messages',

    'django.contrib.staticfiles',

    'Hello',

    )
  ```

### 5.配置路由

```
from django.conf.urls import include, url

    from django.contrib import admin

    from Hello import views as Hello_views

    

    urlpatterns = [

        url(r'^admin/', include(admin.site.urls)),

        url(r'^$', Hello_views.index)

    ]

```

### 6.开启服务

```
python3 manage.py runserver 8080
```




