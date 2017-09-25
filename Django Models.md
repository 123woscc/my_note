# Django Models

![](http://owo62h13n.bkt.clouddn.com/f0157bf7-5e3a-4b4c-8acc-a89c1544f59a.png)

### 1.apps整合

```
#修改settings文件
import sys
import os
sys.path.insert(0,os.path.join(BASE_DIR,'apps'))
```

### 2.继承默认User

```
from django.contrib.auth.models import AbstractUser
class UserProfile(AbstractUser):
	pass
```

### 3.一对多,多对多关系

http://www.cnblogs.com/yangmv/p/5327477.html

### 4.循环引用解决方案

![](http://owo62h13n.bkt.clouddn.com/5ee0d09b-edec-491f-97dd-92461ac020d5.png)

![](http://owo62h13n.bkt.clouddn.com/3d9e02d5-1f02-4bd4-b09b-85e308fc4f82.png)

