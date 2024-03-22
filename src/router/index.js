import { createRouter, createWebHashHistory } from 'vue-router'
// import p2 from '../views/PartTwo.vue'

const routes = [
  {
    path: '/p1',
    name: 'p1',
    component: () => import('../views/PartOne.vue')
  },
  {
    path: '/p2',
    name: 'p2',
    component: () => import('../views/PartTwo.vue')
  },
  {
    path: '/p3',
    name: 'p3',
    component: () => import('../views/PartThree.vue')
  },
  {
    path: '/',
    redirect: '/p1'
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
