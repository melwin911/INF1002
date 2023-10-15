import { createRouter, createWebHistory } from 'vue-router'
import Ping from '../components/Ping.vue'
import MainPage from '../components/MainPage.vue'
import LineChart from '../components/LineChart.vue'
import Map from '../components/Map.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/ping',
      name: 'ping',
      component: Ping
    },
    {
      path: '/',
      name: 'MainPage',
      component: MainPage
    },
    {
      path: '/linechart',
      name: 'LineChart',
      component: LineChart
    },
    {
      path: '/map',
      name: 'Map',
      component: Map
    },
  ]
})

export default router