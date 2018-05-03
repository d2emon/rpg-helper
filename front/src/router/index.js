import Vue from 'vue'
import Router from 'vue-router'

// Containers
import Full from '@/containers/Full'
// import Simple from '@/containers/Simple'

// Views
import Hello from '@/views/Hello'
import Login from '@/views/Login'
import Register from '@/views/Register'
import Worlds from '@/views/Worlds'

import store from '@/store'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/home',
      name: 'Home',
      component: Full,
      children: [
        {
          path: '/home',
          name: 'Hello',
          component: Hello
        }
      ]

    },
    {
      path: '/auth',
      redirect: '/auth/login',
      name: 'Auth',
      component: Full,
      children: [
        {
          path: 'login',
          name: 'Login',
          component: Login
        },
        {
          path: 'logout',
          beforeEnter (to, from, next) {
            next('/auth/login')
            store.dispatch('user/logout')
          }
        },
        {
          path: 'register',
          name: 'Register',
          component: Register
        }
      ]
    },
    {
      path: '/worlds',
      redirect: '/worlds/list',
      name: 'Worlds',
      component: Full,
      children: [
        {
          path: 'list',
          name: 'WorldList',
          component: Worlds
        }
      ]
    }
  ]
})
