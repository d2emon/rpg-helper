import Vue from 'vue'
import Router from 'vue-router'

// Containers
import Full from '@/containers/Full'
// import Simple from '@/containers/Simple'

// Views
import Hello from '@/views/Hello'

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

    }
  ]
})
