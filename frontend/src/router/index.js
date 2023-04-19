import { createRouter, createWebHistory } from 'vue-router'
import store from '@/store'
import { updateStore } from '@/utils'
import HomeView from '../views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import RegisterView from '@/views/RegisterView.vue'
import PostView from '@/views/PostView.vue'
import ProfileView from '@/views/ProfileView.vue'


const routes = [
  {
    path: '/home',
    name: 'home',
    component: HomeView,
    // meta: {requiresLogin:true}

  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/register',
    name: 'register',
    component: RegisterView
  },
  {
    path: '/posts/:id',
    name: 'post',
    component: PostView,
    meta: {requiresLogin:true}
  },
  {
    path: '/user/:id',
    name: 'user',
    component: ProfileView,
    meta: {requiresLogin:true}
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: function () {
      return import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
    }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.base_url),
  routes
})

router.beforeEach(async (to, from, next) => {
    console.log("calling before each")
    if (to.matched.some(record => record.meta.requiresLogin) && store.getters.isAuthenticated == false) {

        next("/Login")
    } else {
        next()
    }
})

  router.afterEach(async (to, from) => {
    console.log("after each start")

    if (from.matched.some(record => record.meta.requiresLogin) && store.getters.isAuthenticated == false) 
    await updateStore()

    console.log("done calling after each")
})


export default router
