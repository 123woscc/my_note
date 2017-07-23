# os模块

### 1.操作文件

```python
os.rename('123.txt','abc.txt')

os.remove('123.txt')
```

### 2.遍历目录

```python
for file in os.listdir('.'):
	if file.endwith('.txt'):
        print(file)
```

```python
for dirpath,dirname,filename in os.walk('.'):
	print(dirpath)
    print(dirname)
    print(filename)
```

### 3.增删目录

```python
#单层目录
os.mkdir('test')
os.rmdir('test')
#多层目录
os.makedirs('test/asd/test')
os.removedirs('test/qwe/test')
#复制
import shutil
shutil.copy('a.txt',os.path.join('backup','a_backup.txt'))
#移除非空目录
shutil.rmtree('backup/')
```

### 4.os.path

```python
#判断文件夹存在与否
os.path.isdir('img')  #True
os.path.isdir('test.txt')  #False
#判断文件存在与否
os.path.isfile('img') #False
os.path.isfile('test.txt')
#判断文件/文件夹存在与否
os.path.exists('img')  #True
os.path.exists('qwe.txt')#True
#文件路径拼接
os.path.join('/path/to/file','file.txt')   
os.path.join('/path/to','file','file.txt')
#文件路径拆分
os.path.splitext('/path/to/file/file.txt')  #('/path/to/file','file.txt')
#获取文件大小
os.path.getsize('123.txt')

```

