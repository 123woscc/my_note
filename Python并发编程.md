# Python并发编程——concurrent.futures模块

使用方式：

> map方法

```python
import time
from concurrent.futures import ProcessPoolExecutor,as_completed


workers=range(1,100000)


K = 50
def f(x):
    r = 0
    for k in range(1, K+2):
        r += x ** (1 / k**1.5)
    return r


if __name__ == '__main__': 

    start=time.time()
    res=[]
    with ProcessPoolExecutor(max_workers=3) as executor:
        #chunksize任务块,divmod(a,b)相当于a/b加a%b,就是获得商和余数
        #加上chunksize可以提高运行效率
        #使用 ThreadPoolExecutor，chunksize 没有效果。
        chunksize,extra=divmod(len(workers),executor._max_workers)
        print(chunksize)

        for num, result in zip(workers, executor.map(f, workers,chunksize=chunksize)):
            res.append(result)

    print(len(res))
    print('COST:{}'.format(time.time() - start))
```

> 使用funtures.as_completed函数

```python
import time
from concurrent.futures import ProcessPoolExecutor,as_completed


workers=range(1,100000)

K = 50
def f(x):
    r = 0
    for k in range(1, K+2):
        r += x ** (1 / k**1.5)
    return r


if __name__ == '__main__':

    start=time.time()
    res=[]
    with ProcessPoolExecutor(max_workers=3) as executor:
        to_do=[]
        for worker in workers:
            future=executor.submit(f,worker)
            to_do.append(future)
            print('msg:',future)
        results=[]
        for future in as_completed(to_do):
            res=future.result()
            results.append(res)

    print(len(results))
    print('COST:{}'.format(time.time() - start))

```

