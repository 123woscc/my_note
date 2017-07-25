# 标准库

> Python自带的 `functools` 模块提供了一些常用的高阶函数，也就是用于处理其它函数的特殊函数.

### functools.cmp_to_key()

语法：

```
functools.cmp_to_key(func)  
```

该函数用于将旧式的比较函数转换为关键字函数。

> 旧式的比较函数：接收两个参数，返回比较的结果。返回值小于零则前者小于后者，返回值大于零则相反，返回值等于零则两者相等。
>
> 关键字函数：接收一个参数，返回其对应的可比较对象。例如 sorted(), min(), max(), heapq.nlargest(), heapq.nsmallest(), itertools.groupby() 都可作为关键字函数。



```
sorted(iterable, key=cmp_to_key(cmp_func))  
```

### functools.total_ordering()

语法：

```
functools.total_ordering(cls)  

```

这是一个类装饰器，用于自动实现类的比较运算。

我们只需要在类中实现 `__eq__()` 方法和以下方法中的任意一个 `__lt__()`, `__le__()`, `__gt__()`, `__ge__()`，那么 `total_ordering()` 就能自动帮我们实现余下的几种比较运算。

> ```python
> import operator       #首先要导入运算符模块
> operator.gt(1,2)      #意思是greater than（大于）
> operator.ge(1,2)      #意思是greater and equal（大于等于）
> operator.eq(1,2)      #意思是equal（等于）
> operator.le(1,2)      #意思是less and equal（小于等于）
> operator.lt(1,2)      #意思是less than（小于）
> ```

示例：

```python
@total_ordering
class Student:  
    def __eq__(self, other):
        return ((self.lastname.lower(), self.firstname.lower()) ==
                (other.lastname.lower(), other.firstname.lower()))
    def __lt__(self, other):
        return ((self.lastname.lower(), self.firstname.lower()) <
                (other.lastname.lower(), other.firstname.lower()))
```

### functools.reduce()

语法：

```
functools.reduce(function, iterable[, initializer])  

```

该函数与 Python 内置的 `reduce()` 函数相同，主要用于编写兼容 Python 3 的代码。

> reduce()传入的函数 f 必须接收两个参数，reduce()对list的每个元素反复调用函数f，并返回最终结果值。
>
> ```python
> def f(x, y):
>     return x + y
> ```
>
> 调用 reduce(f, [1, 3, 5, 7, 9])时，reduce函数将做如下计算：
> 先计算头两个元素：f(1, 3)，结果为4；
> 再把结果和第3个元素计算：f(4, 5)，结果为9；
> 再把结果和第4个元素计算：f(9, 7)，结果为16；
> 再把结果和第5个元素计算：f(16, 9)，结果为25；
> 由于没有更多的元素了，计算结束，返回结果25。

### functools.partial()

语法：

```
functools.partial(func[, *args][, **keywords])  
```

该函数返回一个 `partial` 对象，调用该对象的效果相当于调用 `func` 函数，并传入位置参数 `args` 和关键字参数 `keywords` 。如果调用该对象时传入了位置参数，则这些参数会被添加到 `args` 中。如果传入了关键字参数，则会被添加到 `keywords` 中。

`partial()` 函数的等价实现大致如下：

```python
def partial(func, *args, **keywords):  
    def newfunc(*fargs, **fkeywords):
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(*(args + fargs), **newkeywords)
    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc
```

`partial()` 函数主要用于“冻结”某个函数的部分参数，返回一个参数更少、使用更简单的函数对象。

示例：

```
>>> from functools import partial
>>> basetwo = partial(int, base=2)
>>> basetwo.__doc__ = 'Convert base 2 string to an int.'
>>> basetwo('10010')
18  
```

### functools.update_wrapper()

语法：

```
functools.update_wrapper(wrapper, wrapped[, assigned][, updated])  

```

该函数用于更新包装函数（wrapper），使它看起来像原函数一样。可选的参数是一个元组，`assigned` 元组指定要直接使用原函数的值进行替换的属性，`updated` 元组指定要对照原函数进行更新的属性。这两个参数的默认值分别是模块级别的常量：`WRAPPER_ASSIGNMENTS` 和 `WRAPPER_UPDATES`。前者指定了对包装函数的 `__name__`, `__module__`, `__doc__` 属性进行直接赋值，而后者指定了对包装函数的 `__dict__` 属性进行更新。

该函数主要用于装饰器函数的定义中，置于包装函数之前。如果没有对包装函数进行更新，那么被装饰后的函数所具有的元信息就会变为包装函数的元信息，而不是原函数的元信息。

### functools.wraps()

语法：

```
functools.wraps(wrapped[, assigned][, updated])  
```

`wraps()` 简化了 `update_wrapper()` 函数的调用。它等价于 `partial(update_wrapper, wrapped=wrapped, assigned, updated=updated)`。

示例：

```python
>>> from functools import wraps
>>> def my_decorator(f):
...     @wraps(f)
...     def wrapper(*args, **kwds):
...         print 'Calling decorated function'
...         return f(*args, **kwds)
...     return wrapper

>>> @my_decorator
... def example():
...     """Docstring"""
...     print 'Called example function'

>>> example()
Calling decorated function  
Called example function  
>>> example.__name__
'example'  
>>> example.__doc__
'Docstring'  
```

如果不使用这个函数，示例中的函数名就会变成 `wrapper` ，并且原函数 `example()` 的说明文档（docstring）就会丢失。

### functools.lru_cache()

语法:

```
@functools.lru_cache(maxsize=128, typed=False)
```

> 把耗时的函数的结果保存起来,避免传入相同的参数是重复计算.
>
> maxsize:保存结果的最大数量
>
> typed:设置为True时可以将不同参数类型的结果保存起来

例如:

```python
import functools
import time
def timer(func):
    @functools.wraps(func)
    def deco(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        name=func.__name__
        arg_str=','.join([repr(arg) for arg in args])
        print('[{:.8f}] {}({})'.format(end - start,name,arg_str))
        return result
    return deco

@timer
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == '__main__':
    print(fibonacci(6))

#输出
[0.00000000] fibonacci(0)
[0.00000000] fibonacci(1)
[0.00000000] fibonacci(2)
[0.00000000] fibonacci(1)
[0.00000000] fibonacci(0)
[0.00000000] fibonacci(1)
[0.00000000] fibonacci(2)
[0.00000000] fibonacci(3)
[0.00000000] fibonacci(4)
[0.00000000] fibonacci(1)
[0.00000000] fibonacci(0)
[0.00000000] fibonacci(1)
[0.00000000] fibonacci(2)
[0.00000000] fibonacci(3)
[0.00000000] fibonacci(0)
[0.00000000] fibonacci(1)
[0.00000000] fibonacci(2)
[0.00000000] fibonacci(1)
[0.00000000] fibonacci(0)
[0.00000000] fibonacci(1)
[0.00000000] fibonacci(2)
[0.00000000] fibonacci(3)
[0.00000000] fibonacci(4)
[0.00000000] fibonacci(5)
[0.00000000] fibonacci(6)
8
#使用functools.lru_cache()
...
@functools.lru_cache()   #注意这里要加括号()
@timer
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)
...
[0.0000000000] fibonacci(0)
[0.0000000000] fibonacci(1)
[0.0000000000] fibonacci(2)
[0.0000000000] fibonacci(3)
[0.0000000000] fibonacci(4)
[0.0000000000] fibonacci(5)
[0.0000000000] fibonacci(6)
8

#时间不知道是不是因为太快,所以导致都是0,但是从计算步骤可以看出加了@functools.lru_cache()后从原来的25次减少到后面的6次
```

### functools.singledispatch(default)

语法

```
@functools.singledispatch(default)
```

> 根据参数的类型,已不同方式执行相同操作的一组函数

```python
from functools import singledispatch
import numbers

@singledispatch
def test_type(obj):
    print('type(default):{0}'.format(repr(obj)))

@test_type.register(numbers.Integral)
def _(n):
    print('type(int):{0}'.format(n))

if __name__ == '__main__':
    test_type('123')
    test_type(list(range(3)))
    test_type(123)
#输出
type(default):'123'
type(default):[0, 1, 2]
type(int):123
```





