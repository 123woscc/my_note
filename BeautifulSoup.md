# Beautiful Soup

### 1.解析器对比

| 解析器           | 优势                            | 使用方法                                 | 劣势                                  |
| ------------- | ----------------------------- | ------------------------------------ | ----------------------------------- |
| Python标准库     | Python的内置标准库执行速度适中文档容错能力强     | BeautifulSoup(markup, “html.parser”) | Python 2.7.3 or 3.2.2)前 的版本中文档容错能力差 |
| lxml HTML 解析器 | 速度快文档容错能力强                    | BeautifulSoup(markup, “lxml”)        | 需要安装C语言库                            |
| lxml XML 解析器  | 速度快唯一支持XML的解析器                | BeautifulSoup(markup, “xml”)         | 需要安装C语言库                            |
| html5lib      | 最好的容错性以浏览器的方式解析文档生成HTML5格式的文档 | BeautifulSoup(markup, “html5lib”)    | 速度慢不依赖外部扩展                          |

### 2.创建

```python
soup = BeautifulSoup(html)
#本地导入
soup = BeautifulSoup(open('index.html'))
#格式化输出
soup.prettify()
```

### 3.用法

> ### 节点获取

```python
#获取标签
soup.title
soup.head
soup.a
soup.p
#获取属性
soup.a.name
soup.p.attrs
soup.p['class']
soup.p.get('class')
#获取内容
soup.p.string
#遍历文档树
#子节点
soup.ul.contetns    #tag 的 .content 属性可以将tag的子节点以列表的方式输出(返回列表)
soup.ul.children    # list 生成器对象
#子孙节点
soup.ul.descendants
#多个内容
soup.ul.strings
soup.ul.stripped_strings    #(去除多余空格)
#父节点
soup.li.parent    #单个父节点
soup.li.parents   #所有父节点
#兄弟节点
soup.a.next_sibling      #下一个兄弟节点
soup.a.previous_sibling  #上一个兄弟节点
soup.a.next_siblings     #下部分的所有兄弟节点
soup.a.previous_siblings #上部分的所有兄弟节点
#前后节点
soup.p.next_element		#不分层次
soup.p.previous_element 
soup.p.next_elements	#向前或向后访问文档的解析内容,就好像文档正在被解析一样
soup.p.previous_elements
```

>### 划重点--搜索文档树

````python
find_all(name,attrs,recursive,text,**kwargs)
#1.传标签名
soup.find_all('img')
#2.传正则表达式
soup.find_all(re.compile("^b"))    #搜索所有以b开头的标签
#3.传列表
soup.find_all(['a','p'])
#4.传True
soup.find_all(True)   #True 可以匹配任何值,下面代码查找到所有的tag,但是不会返回字符串节点
#5.传方法
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
soup.find_all(has_class_but_no_id)
#6.传属性
soup.find_all(id='id_name')    #id名
soup.find_all(class_='class_name1 class_name2')    #class属性,因为与python内置class冲突,所以使用class_,可以传多个class,用空格分割
#7.属性正则匹配
soup.find_all(href=re.compile('pan'))
#8.多属性混合
soup.find_all(id='test',class_='red')
#9.其他属性
soup.find_all(attrs={'data-test':'data-value'})
#10.传text
soup.find_all(text='Title')
soup.find_all(text=re.compile('Title'))
#11.限制个数
soup.find_all('a',limit=2)
#12.recursive 参数
soup.html.find_all("title", recursive=False)    #recursive=False,只搜索tag的直接子节点

#其他方法(用法和find_all一样)
#返回单个结果
find( name , attrs , recursive , text , **kwargs )   #用法和find_all一样,但是只返回第一个匹配的结果
#前后兄弟节点(单个/多个)
find_parents()
find_parent()
find_previous_siblings()
find_previous_sibling()
#前后所有节点(单个/多个)
find_all_next()  
find_next()
find_all_previous()
find_previous()
````

> ### CSS选择器

```python
#1.通过标签名查找
soup.select('a')
#2.通过类名查找
soup.select('.title')
#3.通过id查找
soup.select('#title')
#4.组合查找
soup.selet('p #link')
#5.直接子标签查找
soup.selet('p > a')
#6.属性查找
soup.selet('a[href="/post"]')
```



