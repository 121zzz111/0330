// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import VueResource from 'vue-resource'
import 'element-ui/lib/theme-chalk/index.css'
import axios from 'axios'  // 导入axios模块
axios.defaults.baseURL = 'http://localhost:8000/'  // 设置axios请求的默认域名

Vue.prototype.$axios = axios // 全局挂载axios


Vue.use(ElementUI)
Vue.use(VueResource)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  //components: { App },
  //template: '<App/>'
  render: h => h(App)
})
