# Python异常编码处理

### 1.主动触发异常

* raise

  ```python
  raise TypeError
  raise TypeError,'Error Message'    #添加错误提示
  ```

* assert

  ```python
  a = 1
  assert a > 0
  assert a > 0,"a must lg 0"    #添加错误提示
  ```

### 2.处理特定异常

* `try/except`

  ```python
  try:
      int('hello')
  except ValueError:
      print('invaild value')
      
  try:
      int('hello')
  except ValueError as e:
      print(e)
  ```

### 3.处理多个异常

* 用元组包含多种异常

  ```python
  try:  
      file = open('test.txt', 'r')
  except (IOError, EOFError) as e:  
      print "error occurred:", e
  ```

* 多个except语句

  ```python
  try:  
      file = open('test.txt', 'r')
  except (IOError, EOFError) as e:  
      print "error occurred:", e
  ```

* 捕获所有异常

  ```python
  try:  
      3 / 0
  except:  
      print "error occurred"
  ```

* 使用Exception捕获异常

  ```python
  try:  
      "123" / 2
  except Exception as e:  
      print e.message
  ```

### 4.`else/finally`语句

```python
#异常没有触发时执行else后的代码
try:
    f=open('123.txt','w')
    f.write({'name':'ming'})
except Exception as e:
    print('Error:'e)
else:
    f.write({'age':18})
    f.close()
    print('file has closed')
#不管有没有触发异常,都会执行finally后的代码
try:
    f=open('123.txt','w')
    print(f.write({'name':'ming'}))
except Exception as e:
    print('Error:'e)
finally:
    f.close()
    print('file has closed')
```

### 5.自定义异常

> 当现存的异常类型没有自己想要的效果时,可以自己创建属于自己的异常类型

```python
class RangeError(Exception):  
    pass
def process(value):  
    if value < 0 or value > 10000:
        raise RangeError
    pass
```

