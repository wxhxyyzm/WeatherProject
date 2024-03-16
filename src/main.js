import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementPlus from 'element-plus'
import "lib-flexible/flexible.js"//腾讯的插件
import "element-plus/dist/index.css";

createApp(App).use(store).use(router).use(ElementPlus, { size: 'small', zIndex: 3000 }).mount('#app')
const app = createApp(App)

