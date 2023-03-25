import { createapp } from 'vue'
import app from './app.vue'
import router from './router'
import store from './store'
import {emitter } from './utils/index.js'

const app = createapp(app).use(store).use(router)

app.config.globalproperties.$mitt = emitter;
app.mount('#app')
