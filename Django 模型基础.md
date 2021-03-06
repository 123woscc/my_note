# Django 模型基础

### 1.初始化

```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

### 2.添加数据

```
# 1
Person.objects.create(name = name, age = age)

# 2
p = Person(name = name, age = age)
p.save()

# 3
p = Person(name = name)
p.age = age
p.save()

# 4 
Person.objects.get_or_create(name = name, age = age)
```

### 3.查询

```
# 1
Person.objects.all()

# 2. 切片操作，获取10个人，不支持负索引，切片可以节约内存
Person.objects.all()[:10]

# 3
Person.objects.get(name = name)

# 4. get是用来获取一个对象的，如果需要获取满足条件的一些人，就要用到 filter
Person.objects.filter(name = "abc")

# 5. 名称为 abc 但是不区分大小写，可以找到 ABC, Abc, aBC，这些都符合条件
Person.objects.filter(name__iexact = "abc")

# 6. 名称中包含 "abc"的人
Person.objects.filter(name__contains = "abc")

# 7. 名称中包含 "abc"，且abc不区分大小写
Person.objects.filter(name__icontains = "abc")

# 8. 正则表达式查询
Person.objects.filter(name__regex = "^abc")

# 9. 正则表达式不区分大小写
Person.objects.filter(name__iregex = "^abc")

# 10. 排除包含 WZ 的Person对象
Person.objects.exclude(name__contains = "WZ")

# 11. 找出名称含有abc, 但是排除年龄是23岁的
Person.objects.filter(name__contains="abc").exclude(age = 23)
```

