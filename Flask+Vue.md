# Flask+Vue

### 1.前端构建工具 Webpack

```javascript
#初始化
npm init -y
#安装
#npm --registry http://registry.cnpmjs.org install webpack,引用国内源
npm install webpack   
#运行打包
node_modules/.bin/webpack
#打包文件
node_modules/.bin/webpack src/main.js dist/bundle.js #[命令][目标文件][输出文件]
#打包文件2,修改package.json的scripts
"dev": "node_modules/.bin/webpack src/main.js dist/bundle.js"
#npm run <name>
npm run dev
#打包文件3,创建webpack.config.js
var webpack = require('webpack');
var path = require('path');

module.exports = {
    entry: './src/main.js',
    output: {
        // path 需要使用绝对路径
        path: path.resolve(__dirname, './dist'),
        filename: 'bundle.js'
    }
};
#修改package.json的scripts
"dev": "node_modules/.bin/webpack"
npm run dev
```

### 2.淘宝cnpm安装

> 安装

```
npm install -g cnpm --registry=https://registry.npm.taobao.org
```

> 运行

```
cnpm install [name]
```

### 3.vue-cli安装

> 安装

```
cnpm install -g vue-cli
```

> 检测

```
vue -h
```

> 运行

```
vue init webpack-simple hello-app
cd hello-app
npm install
npm run dev
```

### 4.Ajax请求

> 安装

```
npm install --save axios
```

> 使用

```javascript
<script>
var axios = require('axios');

export default {
  name: 'app',
  data () {
    return {
      msg: ''
    }
  },
  mounted() {
      axios.get('/api/hello')
        .then(response => console.log(response.data))
  }
}
</script>
```

### 5.配置代理

打开 `webpack.config.js`, 找到 `devServer`，将其中内容修改如下：

```javascript
devServer: {
  historyApiFallback: true,
  noInfo: true,
  proxy: {"/api/*": {target: 'http://localhost:5000', host: 'localhost'}}
}
```

重启