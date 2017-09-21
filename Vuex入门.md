# Vuex入门

### 1.安装

```
npm install -S vuex
```

### 2.基础架构

```javascript
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

// 所有应用级别的状态都放在这里
const state = {
    // 计数器的初始状态为 0
    count: 0
}

// 类似于组件中的 computed，可以对 state 里面的数据
// 做处理，然后通过 $store.getters.func 的方式获取
const getters = {

}

// state 里面的状态不能直接改变，想要改变就需要在这里
// 定义函数，函数的第一个参数是 state，通过这个参数改
// 变 state 里面的数据
// 在组件中通过 $store.commit() 触发
const mutations = {

}

// 和 mutations 类似，但 actions 触发的是 mutations
// mutations 只能进行同步操作，在 actions 中可以定义
// 异步操作
const actions = {

}

export default new Vuex.Store({
  state,
  getters,
  mutations,
  actions
})
```

### 3.注入store

```
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

new Vue({
  el: '#app',
  render: h => h(App),
  store
})
```

### 4.使用

* state(类似data)

```
const state = {
    count: 0
}
```



* mutations(类似methods)

```
const mutations = {
  increment: state => state.count++,
  decrement: state => state.count--,
}
```

* getters(类似computed)

```
const getters = {
  // 接收 state 作为参数
  evenOrOdd: state => state.count % 2 === 0 ? 'even' : 'odd'
}
```

* actions(异步执行)

```
const actions = {
  // 这个箭头函数中的传参方式为 ES2015 的 参数解构，可以简化代码
  // commit 是从一个 context 对象中解构出来的，context 类似 state 对象，
  // 只是不包含 state 里面的状态数据
  asyncIncrByAmount: ({ commit }, { amount }) => {
    setTimeout(() => {
      commit('incrByAmount', { amount })
    }, 2000)
  }
}
```

