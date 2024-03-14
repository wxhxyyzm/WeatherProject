import { createRouter, createWebHashHistory } from 'vue-router'
// import p2 from '../views/PartTwo.vue'

const routes = [

  {
    path: '/p2',
    name: 'p2',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import('../views/PartTwo.vue')
  },
  {
    path: '/',
    redirect: '/p2'
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
