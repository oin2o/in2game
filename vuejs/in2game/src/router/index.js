import Vue from 'vue'
import VueRouter from 'vue-router'

const TheContainer = () => import('@/containers/Container')

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    component: TheContainer,
    redirect: '/login',
    children: [
      {
        path: 'login',
        component: () => import('@/views/login/main'),
        name: 'Login',
      },
    ],
  },
  {
    path: '/lobby',
    component: TheContainer,
    children: [
      {
        path: '',
        component: () => import('@/views/lobby/main'),
        name: 'Lobby',
        meta: {
          requiresAuth: false,
        },
      },
    ],
  },
  {
    path: '/explain',
    component: TheContainer,
    children: [
      {
        path: '',
        component: () => import('@/views/explain/main'),
        name: 'Explain',
        meta: {
          requiresAuth: false,
        },
      },
    ],
  },
  {
    path: '/rank',
    component: TheContainer,
    children: [
      {
        path: '',
        component: () => import('@/views/rank/main'),
        name: 'Rank',
        meta: {
          requiresAuth: false,
        },
      },
    ],
  },
  {
    path: '/game',
    component: TheContainer,
    children: [
      {
        path: '',
        component: () => import('@/views/game/main'),
        name: 'Game',
        meta: {
          requiresAuth: false,
        },
      },
    ],
  },
  {
    path: '*',
    redirect: '/',
    hidden: true,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
