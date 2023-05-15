import Vue from 'vue'
import Router from 'vue-router'
//import HelloWorld from '@/components/HelloWorld'
//import home from '@/components/home'
import search from '@/components/search'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      //name: 'HelloWorld',
      //name: 'home',
      name: 'search',
      //component: HelloWorld
      component: search
    }
  ]
})
