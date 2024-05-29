import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementPlus from 'element-plus'
import 'lib-flexible/flexible.js'// 腾讯的插件
import './style/element-plus.scss'
import 'element-plus/dist/index.css'
// import VueConciseSlider from 'vue-concise-slider';
// import VueAwesomeSwiper from 'vue-awesome-swiper';
createApp(App).use(store).use(router).use(ElementPlus, { size: 'small', zIndex: 3000 }).mount('#app')
const app = createApp(App)
const debounce = (fn, delay) => {
  let timer
  return (...args) => {
    if (timer) {
      clearTimeout(timer)
    }
    timer = setTimeout(() => {
      fn(...args)
    }, delay)
  }
}

const _ResizeObserver = window.ResizeObserver
window.ResizeObserver = class ResizeObserver extends _ResizeObserver {
  constructor(callback) {
    callback = debounce(callback, 200)
    super(callback)
  }
}
