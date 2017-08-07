# `__init__ , __new__,__call__` ,都是在什么时候被触发?`__getattr__`和`__getattribute__`应用有什么不同?

```python
class A:
    def __init__(self):
        print("__init__ ")
        super(A, self).__init__()

    def __new__(cls):
        print("__new__ ")
        return super(A, cls).__new__(cls)

    def __call__(self):  # 可以定义任意参数
        print('__call__ ')

if __name__ == '__main__':
    a=A()
    print('*'*60)
    a()

输出
__new__ 
__init__ 
************************************************************
__call__ 

```



从输出结果来看， `__new__`方法先被调用，返回一个实例对象，接着 `__init__` 被调用,`__call__`在加上()后才被调用

### `__new__` 

它作为构造函数用于创建对象，是一个工厂函数，专用于生产实例对象。著名的设计模式之一，单例模式，就可以通过此方法来实现。

> 返回值为类的实例对象

例如:

````python
class BaseController(object):
    _singleton = None
    def __new__(cls, *a, **k):
        if not cls._singleton:
            cls._singleton = object.__new__(cls, *a, **k)
        return cls._singleton
````



### `__init__`

 方法可以用来做一些初始化工作，比如给实例对象的状态进行初始化

> 返回值为None,否则会报错:TypeError: __init__() should return None, not '***'



### `__call__`

如果在类中实现了 `__call__` 方法，那么实例对象也将成为一个可调用对象,既可添加()调用

结合类的特性来说，类可以记录数据（属性），而函数不行（闭包某种意义上也可行），利用这种特性可以实现基于类的装饰器，在类里面记录状态，比如，下面这个例子用于记录函数被调用的次数：

```python
class Counter:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)

@Counter
def foo():
    pass

for i in range(10):
    foo()

print(foo.count)  # 10
```



### `__getattr__`

`getattr`会在没有查找到相应实例属性时被调用

```python
class UrlTest():
    def __init__(self,url):
        self.url=url

    def __getattr__(self, item):
        if item =='get' or item == 'post':
            print(self.url)
        return UrlTest('{}/{}'.format(self.url,item))


if __name__ == '__main__':
    my_url=UrlTest('http://woscc.com')
    my_url.userinfo.get
    my_url.login.post

```



### `__getattribute__`

当访问某个实例属性时， getattribute会被无条件调用，如未实现自己的getattr方法，会抛出`AttributeError`提示找不到这个属性，如果自定义了自己getattr方法的话，方法会在这种找不到属性的情况下被调用，比如上面的例子中的情况。

```python
class GetColor():
    def __getattr__(self, item):
        if item=='color':
            return 'Blue'
        else:
            return 'raise AttributeError'

class GetColor2():
    def __getattribute__(self, item):
        if item=='color':
            return 'Blue'
        else:
            return 'raise AttributeError'


if __name__ == '__main__':
    color1=GetColor()
    print(color1.color)
    color1.color='Red'
    print(color1.color)
    print('*'*60)
    color2=GetColor2()
    print(color2.color)
    color2.color='Yellow'
    print(color2.color)

输出结果:
Blue
Red
************************************************************
Blue
Blue  #未改变color的值,依旧返回设置的内容

```

因为getattribute在访问属性的时候一直会被调用，自定义的getattribute方法里面同时需要返回相应的属性，通过`self.__dict__`取值会继续向下调用getattribute，造成循环调用：

```python
class GetColor():
    def __getattr__(self, item):
        if item=='color':
            return 'Blue'
        else:
            return 'raise AttributeError'

class GetColor2():
    def __getattribute__(self, item):
        return 'raise AttributeError'


    def swim(self):
        pass


if __name__ == '__main__':

    color2=GetColor2()

    color2.swim()
    
输出:
    Traceback (most recent call last):
  File "C:/Users/12845/Desktop/douyu_play/my_test.py", line 21, in <module>
    color2.swim()
TypeError: 'str' object is not callable
```

解决方法:

```
class AboutAttr(object):
    def __init__(self, name):
        self.name = name

    def __getattribute__(self, item):
        try:
            return super(AboutAttr, self).__getattribute__(item)
        except KeyError:
            return 'default'
```

这里通过调用绑定的super对象来获取队形的属性，对新式类来说其实和`object.__getattribute__(self, item)`一样的道理:

- 默认情况下自定义的类会从object继承`getattribute`方法，对于属性的查找是完全能用的
- getattribute的实现感觉还是挺抽象化的，只需要绑定相应的实例对象和要查找的属性名称就行













