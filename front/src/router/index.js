import Vue from 'vue'
import Router from 'vue-router'

// Containers
import Full from '@/containers/Full'
// import Simple from '@/containers/Simple'

// Views
import Hello from '@/views/Hello'
import Login from '@/views/Login'

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
        /* },
        {
          path: 'register',
          name: 'Register',
          component: Register */
        }
      ]
    }
  ]
})
