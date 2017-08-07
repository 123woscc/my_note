# @classmethod VS @staticmethod 

> 共同点

和类相关的操作，但是又不会依赖和改变类、实例的状态

> @staticmethod

1. 作用空间为相应的类
2. 子类继承时,创建的仍然是父类的对象
3. 常用于检测

> @classmethod

1. 不管这个方式是从实例调用还是从类调用，它都用第一个参数把类传递过来,就是类本身
2. 子类可以继承相应的方法
3. 常用于类的重构

```python
class Date(object):
    def __init__(self, year=0, month=0, day=0):
        self.day = year
        self.month = month
        self.year = day
    
    #其他格式的创建方式
    @classmethod
    def from_string(cls, date_as_string):
        year, month, day = map(int, date_as_string.split('-'))
        date1 = cls(year, month, day)
        return date1
    
    #日期检验
    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999
    


date1 = Date(2017,7,20)                 
date2 = Date.from_string('2017-07-20')

is_date = Date.is_date_valid('2017-10-01')  #True
is_date2 = Date.is_date_valid('2017-30-22') #False

```

> 为是什么会有区别

```python
Class Date:
  def __init__(self, year, month, day):
    self.year = year
    self.month = month
    self.day = day


  def display(self):
    return "{0}-{1}-{2}".format(self.year, self.month, self.day)


  @staticmethod
  def future(month, day):
    return Date(3000, month, day)

now_year = Date(2017, 7, 20)  # 成功创建now_year
future_year = Date.future(1, 1) 	# 成功创建future_year


now_year.display()# "2017-7-20"
future_year.display()# "3000-1-1"

isinstance(now_year, Date) 	# True
isinstance(future_year, Date) # True


#继承自Date
class DateTime(Date):
  def display(self):
      return "{0}-{1}-{2} - 00:00:00PM".format(self.year, self.month, self.day)


datetime1 = DateTime(10, 10, 1990)
datetime2 = DateTime.millenium(10, 10)

isinstance(datetime1, DateTime) # True
isinstance(datetime2, DateTime) # False

datetime1.display() # "10-10-1990 - 00:00:00PM"
datetime2.display() # "10-10-2000" 因为它不是一个DateTime对象,而是Date对象

#改写
Class Date:
  def __init__(self, year, month, day):
    self.year = year
    self.month   = month
    self.day  = day


  def display(self):
    return "{0}-{1}-{2}".format(self.year, self.month, self.day)


 @classmethod
 def future(cls, month, day):
    return cls(3000, month, day)



datetime1 = DateTime(10, 10, 1990)   
datetime2 = DateTime.millenium(10, 10)

datetime2.display() # "1990-10-10-00:00:00PM"

isinstance(datetime1, DateTime) # True
isinstance(datetime2, DateTime) # True

```

> 参考资料

1. # [Meaning of @classmethod and @staticmethod for beginner?](https://stackoverflow.com/questions/12179271/meaning-of-classmethod-and-staticmethod-for-beginner)

2. # [Python 中的 classmethod 和 staticmethod 有什么具体用途？](https://www.zhihu.com/question/20021164)