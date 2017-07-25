# 正则表达式——re模块

### 1.re.match

re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。

```python
re.match(pattern, string, flags=0)
```

匹配成功re.match方法返回一个匹配的对象，否则返回None。

我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。

### 2.re.search方法

re.search 扫描整个字符串并返回第一个成功的匹配。

```python
re.search(pattern, string, flags=0)
```

匹配成功re.search方法返回一个匹配的对象，否则返回None。

我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。

>re.match与re.search的区别
>
>re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。

### 3.re.sub

re.sub用于替换字符串中的匹配项。

```
re.sub(pattern, repl, string, count)
```

第一个参数为匹配规则;

第二个参数是替换后的字符串;

第三个参数是替换的目标字符串;

第四个参数指替换个数。默认为0，表示每个匹配项都替换。

### 4.re.spilt

可以使用re.split来分割字符串，如：re.split(r'\s+', text)；将字符串按空格分割成一个单词列表

### 5.re.findall

re.findall可以获取字符串中所有匹配的字符串。

### 6.re.compile

可以把正则表达式编译成一个正则表达式对象。可以把那些经常使用的正则表达式编译成正则表达式对象，这样可以提高一定的效率。

