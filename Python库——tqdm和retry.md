# Python库——tqdm和retry

### 1.tqdm

> 作用：进度条
>
> 使用方法：在循环体里边加个`tqdm`
>
> GIthub地址：https://github.com/tqdm/tqdm

```python
import time
from tqdm import tqdm

for i in tqdm(range(1000)):
    time.sleep(.01)
```

### 2.retry

>作用：超时重新运行
>
>使用方法：@retry(tries, delay)【参数说明：tries=次数；delay=超时时间】
>
>GIthub地址：https://github.com/invl/retry

```python
from retry import retry

@retry(tries=5, delay=2)
def do_something():
    xxx

do_something()

#相当于
import time
def do_something():
  xxx

for i in range(5):
  try:
    do_something()
    break
  except:
    time.sleep(2)
```

