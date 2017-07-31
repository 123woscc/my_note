# axios

### 1.GET

```javascript
#方式一
axios.get('/messages')
  .then(function(response){
    console.log(response)
  })
  .catch(function(error){
    console.log(error)
  })
#方式二
axios.get('/user',{
  params:{
    id:123
  }
})
.then(function(response){
  console.log(response);
})
.catch(function(err){
  console.log(err);
});
#方式三
axios.get('/api/messages')
  .then(response => console.log(response.data))
  .catch(error => console.log(error.response.data))
```

### 2.POST

```javascript
axios.post('/user',{
  firstName:'Fred',
  lastName:'Flintstone'
})
.then(function(res){
  console.log(res);
})
.catch(function(err){
  console.log(err);
});
```

### 3.多个请求同时发送

```javascript
function getUserAccount(){
  return axios.get('/user/12345');
}
function getUserPermissions(){
  return axios.get('/user/12345/permissions');
}
axios.all([getUserAccount(),getUserPermissions()])
  .then(axios.spread(function(acct,perms){
    //当这两个请求都完成的时候会触发这个函数，两个参数分别代表返回的结果
  }))

//iterable是一个可以迭代的参数如数组等
axios.all(iterable)
//callback要等到所有请求都完成才会执行
axios.spread(callback)
```

### 4.API

```javascript
#POST
axios({
    method:"POST",
    url:'/user/12345',
    data:{
        firstName:"Fred",
        lastName:"Flintstone"
    }
});
#GET
axios('/user/12345');

#其他别名
axios.request(config);

axios.get(url[,config]);

axios.delete(url[,config]);

axios.head(url[,config]);

axios.post(url[,data[,config]]);

axios.put(url[,data[,config]])

axios.patch(url[,data[,config]])
```

### 5.返回值

```
{
  data:{},
  status:code,
  statusText:'OK',
  headers: {},
  config: {}
}
```

### 6.配置

```javascript
//全局配置
axios.defaults.baseURL = 'http://api.exmple.com';

axios.defaults.headers.common['Authorization'] = AUTH_TOKEN;

axios.defaults.headers.post['content-Type'] = 'appliction/x-www-form-urlencoded';

//当创建实例的时候配置默认配置
var instance = axios.create({
    baseURL: 'https://api.example.com'
});

//当实例创建时候修改配置
instance.defaults.headers.common["Authorization"] = AUTH_TOKEN;
```

