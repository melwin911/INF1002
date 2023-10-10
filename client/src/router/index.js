import { createRouter, createWebHistory } from 'vue-router'
import Ping from '../components/Ping.vue'
import HDB from '../components/Accordion.vue';
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
    },
    {
      path: '/Accordion',
      name: 'HDB',
      component: HDB,
    },
  ]
})

export default router