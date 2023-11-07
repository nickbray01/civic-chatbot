import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Ping from '../components/Ping.vue'
import Books from '../components/Books.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping
    },
    {
      path: '/books',
      name: 'Books',
      component: Books,
    },
  ]
})

export default router
