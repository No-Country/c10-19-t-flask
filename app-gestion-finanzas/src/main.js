import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'



import './assets/main.css'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-icons/font/bootstrap-icons.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'




const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
