# Django目录浏览

 **目录**

```
.
├── Hello
│   ├── admin.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── HelloWorld
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-34.pyc
│   │   └── settings.cpython-34.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

**urls.py**

链接入口，关联到对应的 `views.py` 中的一个函数（或者称作 generic 类），访问的链接就对应一个函数。

**views.py**

处理用户发出的请求，从 `urls.py` 中对应而来，通过渲染 *templates* 中的网页可以为用户显示页面内容，比如登录后的用户名，用户请求的数据，通过其输出到页面。

**models.py**

与数据库操作相关，存入或读取数据时使用。当不使用数据库的时候，也可以当做一般的类封装文件，存储各种类的定义。

**forms.py**

表单，用户在浏览器上输入提交，对数据的验证工作以及输入框的生成等工作，都依托于此。

**admin.py**

后台文件，可以用少量的代码就拥有一个强大的后台。

**settings.py**

Django 的设置、配置文件，比如 DEBUG 的开关，静态文件的位置等等。

除了这些，还有以上目录中未提及的：

**templates目录**

`views.py` 中的函数渲染 templates 中的 html 模板，得到动态内容的网页，可以用缓存来提高渲染速度。