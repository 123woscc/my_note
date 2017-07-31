# super的作用

### MRO 列表

事实上，对于你定义的每一个类，Python 会计算出一个**方法解析顺序（Method Resolution Order, MRO）列表**，**它代表了类继承的顺序**，我们可以使用下面的方式获得某个类的 MRO 列表,那这个 MRO 列表的顺序是怎么定的呢，它是通过一个 [C3 线性化算法](https://www.python.org/download/releases/2.3/mro/)来实现的，这里我们就不去深究这个算法了，感兴趣的读者可以自己去了解一下，总的来说，一个类的 MRO 列表就是合并所有父类的 MRO 列表，并遵循以下三条原则：

- 子类永远在父类前面
- 如果有多个父类，会根据它们在列表中的顺序被检查
- 如果对下一个类存在两个合法的选择，选择第一个父类



### super的原理

```python
def super(cls, inst):
    mro = inst.__class__.mro()
    return mro[mro.index(cls) + 1]
```

其中，cls 代表类，inst 代表实例，上面的代码做了两件事：

- 获取 inst 的 MRO 列表
- 查找 cls 在当前 MRO 列表中的 index, 并返回它的下一个类，即 mro[index + 1]

当你使用 `super(cls, inst)` 时，Python 会在 inst 的 MRO 列表上搜索 cls 的下一个类。



### 例子展示

```python
class Base(object):
    def __init__(self):
        print "enter Base"
        print "leave Base"
 
class A(Base):
    def __init__(self):
        print "enter A"
        super(A, self).__init__()
        print "leave A"
 
class B(Base):
    def __init__(self):
        print "enter B"
        super(B, self).__init__()
        print "leave B"
 
class C(A, B):
    def __init__(self):
        print "enter C"
        super(C, self).__init__()
        print "leave C"
        
print(C.mro())
c=C()
#输出
[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Base'>, <class 'object'>]

enter C
enter A
enter B
enter Base
leave Base
leave B
leave A
leave C
```

### 小结

`super(cls, inst)` 获得的是 cls 在 inst 的 MRO 列表中的下一个类。

> super(A, self)    
>
> 获得A再
>
> [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Base'>, <class 'object'>]的下一个类B