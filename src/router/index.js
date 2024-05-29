import { createRouter, createWebHashHistory } from 'vue-router'
// import p2 from '../views/PartTwo.vue'
import Vue from 'vue';
import { nextTick } from 'vue';
const routes = [
  {
    path: '/home',
    name: 'home',
    component: () => import('../views/Home.vue')
  },
  {
    path: '/loginuser',
    name: 'loginuser',
    component: () => import('../views/Loginuser.vue')
  },
  {
    path: '/loginmanager',
    name: 'loginmanager',
    component: () => import('../views/Loginmanager.vue')
  },
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
    path: '/p4',
    name: 'p4',
    component: () => import('../views/PartFour.vue')
  },
  {
    path: '/p42',
    name: 'p42',
    component: () => import('../views/PartFour2.vue')
  },
  {
    path: '/pz',
    name: 'pz',
    component: () => import('../views/PersonZoom.vue')
  },
  {
    path: '/register',
    name: 'register',
    component: () => import('../views/Register.vue')
  },
  {
    path: '/',
    redirect: '/home'
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
});


let isInitialLoad = true;

router.afterEach((to, from) => {
  // 确保路由确实发生了变化，并且不是初始加载
  if (to.path !== from.path && !isInitialLoad) {
    location.reload(); // 强制刷新页面
    console.log("刷新")
  }
  isInitialLoad = false; // 首次加载后设置为false
});

export default router
