import { createApp } from 'vue'
import App from './App.vue'
import {axios} from 'axios'
Vue.prototype.$axios = axios
createApp(App).mount('#app')
