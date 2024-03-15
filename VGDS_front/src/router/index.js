import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import Target from '../views/Target'
import Article from '../views/Article'
import Search from '@/views/Search'
import Help from '../views/Help'
import Detail from '@/views/Detail'
import Differential from '@/views/Differential'
import Correlation from '@/views/Correlation'
import Survival from '@/views/Survival'
import Enrichment from '@/views/Enrichment'
import Datasets from '@/views/Datasets'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/target',
    name: 'Target',
    component: Target
  },
  {
    path: '/article',
    name: 'Article',
    component: Article
  },
  {
    path: '/datasets',
    name: 'Datasets',
    component: Datasets
  },
  {
    path: '/differential',
    name: 'Differential',
    component: Differential
  },
  {
    path: '/correlation',
    name: 'Correlation',
    component: Correlation
  },
  {
    path: '/survival',
    name: 'Survival',
    component: Survival
  },
  {
    path: '/enrichment',
    name: 'Enrichment',
    component: Enrichment
  },
  {
    path: '/search',
    name: 'Search',
    component: Search
  },
  {
    path: '/detail',
    name: 'Detail',
    component: Detail
  },
  {
    path: '/help',
    name: 'Help',
    component: Help
  },
  {
    path: '/about',
    name: 'About',
    component: About
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
