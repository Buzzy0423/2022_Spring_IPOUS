import {createRouter, createWebHashHistory, createWebHistory} from 'vue-router'
import head from '../components/layouts/BaseHeader.vue'
import content from "../components/Content.vue";
import team from "../components/team.vue"

const routes = [
  {
    path:'/',
    component: content,
  },
  {
    path: '/content',
    component: content,
  },{
  path:'/team',
    component: team,
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router