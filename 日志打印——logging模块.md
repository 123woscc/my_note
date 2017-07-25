# 日志打印——logging模块

```python
import logging
#记录日志到文件,默认等级为warning,所以info信息不会被打印出来
logging.warning('Warning Message')
logging.info('Info Message')
#记录日志到文件
logging.basicConfig(filename='example.log',level=logging.DEBUG)  #设置文件路径名字和错误信息捕获等级
#自定义日志格式
logging.basicConfig(format='[%(asctime)s]%(levelname)s:%(message)s')
```

