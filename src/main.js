import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import "lib-flexible/flexible.js"//腾讯的插件
createApp(App).use(store).use(router).mount('#app')
