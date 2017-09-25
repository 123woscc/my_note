# xadmin安装以及配置

### 1.安装

```
git clone https://github.com/sshwsfc/xadmin/tree/master
pip install -r requirements.txt
导入 xadmin包到Django项目文件的extra_apps中
```

### 2.基础配置

```
修改settings.py文件
sys.path.insert(0,os.path.join(BASE_DIR,'extra_apps'))
注册app
{
	'xadmin',
    'crispy_forms',
}
配置路由
 url(r'^xadmin/', xadmin.site.urls)
 
初始化数据库
makemigrations
migrate
```

### 3.models注册

```
在app中添加adminx.py文件

编写adminx.py
class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']

注册
xadmin.site.register(Banner, BannerAdmin)

外键搜索
class__name
```

### 4.全局配置

```
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobaSetting(object):
    site_title = '慕学后台管理系统'
    site_footer = '慕学在线'
    menu_style ='accordion'
```

```
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobaSetting)
```