import { createRouter, createWebHistory } from 'vue-router'
/*import Books from '../components/Books.vue'*/
import Ping from '../components/Ping.vue'
/*import HDB from '../components/HDB.vue'*/
import MainPage from '../components/MainPage.vue'
import Map from "../components/Map.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/ping',
      name: 'ping',
      component: Ping
    },
    {
      path: '/main',
      name: 'MainPage',
      component: MainPage
    },
    {
      path : "/map",
      name : "Map",
      component : Map,
    }
  ]
})

export default router