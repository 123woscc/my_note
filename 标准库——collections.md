# 标准库——collections

### 1.namedtuple

namedtuple主要用来产生可以使用名称来访问元素的数据对象，通常用来增强代码的可读性， 在访问一些tuple类型的数据时尤其好用。

```python
import collections

Surface=collections.namedtuple('Surface','model cup ram rom price')

pro3=Surface('Por3','i5','4g','128g','4000RMB')
pro4=Surface('Por4','i7','8g','256g','8000RMB')

print(pro3)
print(pro4)

输出
Surface(model='Por3', cup='i5', ram='4g', rom='128g', price='4000RMB')
Surface(model='Por4', cup='i7', ram='8g', rom='256g', price='8000RMB')
```

### 2.deque

deque其实是 `double-ended queue` 的缩写，翻译过来就是双端队列，它最大的好处就是实现了从队列 头部快速增加和取出对象: `.popleft()`, `.appendleft()` 。

> 可以设置最大长度 maxlen

常用命令:

>append(往右边添加一个元素)
>
>appendleft（往左边添加一个元素）
>
>clear(清空队列)
>
>copy(浅拷贝)
>
>count(返回指定元素的出现次数)
>
>extend(从队列右边扩展一个列表的元素)
>
>extendleft(从队列左边扩展一个列表的元素)
>
>index（查找某个元素的索引位置）
>
>insert（在指定位置插入元素）
>
>pop（获取最右边一个元素，并在队列中删除）
>
>popleft（获取最左边一个元素，并在队列中删除）
>
>remove（删除指定元素）
>
>reverse（队列反转）
>
>rotate(1)（把右边元素放到左边,默认次数为1）

### 3.Counter

计数器是一个非常常用的功能需求,例如:

```python
import collections
s='asdasDnkanskdoi2j3ajnksji9iweu98wuq8ydfy43ehwkjndkj3btug7saty3bjwq3'

c=collections.Counter(s)

print(c)
# 获取出现频率最高的5个字符
print(c.most_common(5))

输出
Counter({'j': 6, 'a': 5, 's': 5, 'k': 5, '3': 5, 'd': 4, 'n': 4, 'w': 4, 'i': 3, 'u': 3, 'y': 3, '9': 2, 'e': 2, '8': 2, 'q': 2, 'b': 2, 't': 2, 'D': 1, 'o': 1, '2': 1, 'f': 1, '4': 1, 'h': 1, 'g': 1, '7': 1})
[('j', 6), ('a', 5), ('s', 5), ('k', 5), ('3', 5)]
```

### 4.OrderedDict

在Python中，dict这个数据结构由于hash的特性，是无序的，这在有的时候会给我们带来一些麻烦， 幸运的是，collections模块为我们提供了OrderedDict，当你要获得一个有序的字典对象时，用它就对了。

### 5.defaultdict

在使用Python原生的数据结构dict的时候，如果用 `d[key]` 这样的方式访问， 当指定的key不存在时，是会抛出KeyError异常的。

但是，如果使用defaultdict，只要你传入一个默认的工厂方法，那么请求一个不存在的key时， 便会调用这个工厂方法使用其结果来作为这个key的默认值。

如果在创建defaultdict的时候没有指定default_factory,查询不存在的键会触发KeyError





