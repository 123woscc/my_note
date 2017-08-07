# Flask Script

### 1.安装

```
pip install flask-script
```

### 2.使用

```python
from flask_script import Manager,Server
from main import app
#注册app
manager=Manager(app)
#添加服务器启动命令
manager.add_command('server',Server())
#添加shell字典
@manager.shell
def make_shell_context():
    ruturn dict(app=app)
#启动
 if __name__ == '__main__':
    manager.run()   
```

