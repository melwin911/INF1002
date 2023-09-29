import { createRouter, createWebHistory } from 'vue-router'
import Books from '../components/Books.vue'
import Ping from '../components/Ping.vue'
import HDB from '../components/HDB.vue'
import MainPage from '../components/MainPage.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/books',
      name: 'Books',
      component: Books,
    },
    {
      path: '/ping',
      name: 'ping',
      component: Ping
    },
    {
      path: '/hdb',
      name: 'HDB',
      component: HDB
    },
    {
      path: '/main',
      name: 'MainPage',
      component: MainPage
    },
  ]
})

export default router