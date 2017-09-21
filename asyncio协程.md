# asyncio协程

简单案例

```python
import asyncio

async def do_some_work(x):
    print('Watitimg:',x)
    #耗时任务
    await asyncio.sleep(x)
    return 'Task done after {}s'.format(x)
#创建任务
worker=do_some_work(3)
#事件循环
loop=asyncio.get_event_loop()
#生成期望
task=asyncio.ensure_future(worker)
#注册任务
loop.run_until_complete(task)
```

多任务

```python
worker1=do_some_work(3)
worker2=do_some_work(2)
worker3=do_some_work(1)

tasks=[asyncio.ensure_future(worker1)
      asyncio.ensure_future(worker2)
      asyncio.ensure_future(worker3)]
#注册任务列表
#loop.run_until_complete(asyncio.gather(*tasks))
loop.run_until_complete(asyncio.wait(tasks))
#输出结果
for task in tasks:
  print('Task result:',task.result())
```

协程嵌套

```python
import asyncio

async def do_some_work(x):
    print('Watitimg:',x)
    await asyncio.sleep(x)
    return 'Task done after {}s'.format(x)

async def main():
    worker1=do_some_work(3)
    worker2=do_some_work(2)
    worker3=do_some_work(1)

    tasks=[asyncio.ensure_future(worker1)
          asyncio.ensure_future(worker2)
          asyncio.ensure_future(worker3)]
    
    dones,pendings=await asyncio.wait(tasks)
    
    #asyncio.gather创建协程对象，await的返回值就是协程运行的结果
    #results = await asyncio.gather(*tasks)
    #for result in results:
    #    print('Task ret: ', result)
    
    for task in dones:
      print('Task result:',task.result())
      
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
#在外层处理结果输出
#results = loop.run_until_complete(main())
#for result in results:
#    print('Task ret: ', result)
```

使用asyncio.wait方式挂起协程

```python
async def main():
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(4)

    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]

    return await asyncio.wait(tasks)


loop = asyncio.get_event_loop()
done, pending = loop.run_until_complete(main())

for task in done:
    print('Task ret: ', task.result())
```

使用asyncio的as_completed方法

```python
async def main():
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(4)
 
    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]
    for task in asyncio.as_completed(tasks):
        result = await task
        print('Task ret: {}'.format(result))
 
 
loop = asyncio.get_event_loop()
done = loop.run_until_complete(main())
```

停止协程

```python
try:
    loop.run_until_complete(asyncio.wait(tasks))
except KeyboardInterrupt as e:
    print(asyncio.Task.all_tasks())
    for task in asyncio.Task.all_tasks():
        print(task.cancel())
    loop.stop()
    loop.run_forever()
finally:
    loop.close()
```

线程+协程

```python
#开启无限事件循环
def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()
 #耗时任务
async def do_some_work(x):
    print('Waiting {}'.format(x))
    await asyncio.sleep(x)
    print('Done after {}s'.format(x))

new_loop = asyncio.new_event_loop()
#在新线程中启动事件循环
t = Thread(target=start_loop, args=(new_loop,))
t.start()
#添加任务
asyncio.run_coroutine_threadsafe(do_some_work(6), new_loop)
asyncio.run_coroutine_threadsafe(do_some_work(4), new_loop)
```

停止子线程

```python
new_loop = asyncio.new_event_loop()
t = Thread(target=start_loop, args=(new_loop,))
t.setDaemon(True)    # 设置子线程为守护线程
t.start()
 
try:
    while True:
        # print('start rpop')
        task = rcon.rpop("queue")
        if not task:
            time.sleep(1)
            continue
        asyncio.run_coroutine_threadsafe(do_some_work(int(task)), new_loop)
except KeyboardInterrupt as e:
    print(e)
    new_loop.stop()
```





