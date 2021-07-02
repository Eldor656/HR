import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Khamza from '../views/Khamza'
import Izzat from '../views/Izzat'
import Sardor from '../views/Sardor'

Vue.use(VueRouter)

const routes = [
  {
    path: '/khamza',
    name: Khamza,
    component: Khamza
  },
  {
    path: '/izzat',
    name: Izzat,
    component: Izzat
  },
  {
    path: '/sardor',
    name: Sardor,
    component: Sardor
  },
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

