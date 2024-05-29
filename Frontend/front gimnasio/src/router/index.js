import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../components/login.vue'
import RegisterUserView from '../components/RegisterUser.vue'
import MenuView from './../components/menu.vue'
import Persona from './../components/Persona.vue'
import Dashboard from './../components/Dashboard.vue'
import Dietas from './../components/Dietas.vue'
import IndicadorN from './../components/IndicadorN.vue'
import PreguntaN from './../components/PreguntaN.vue'
import ValoracionN from './../components/ValoracionN.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: LoginView
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterUserView
    },

    {
      path: '/menu',
      name: 'menu',
      component: MenuView,
      children: [
        {path: '/personas', name: 'personas', component: Persona},
        {path: '/dashboard', name: 'dashboard', component: Dashboard},
        {path: '/dietas', name: 'dietas', component: Dietas},
        {path: '/indicadorN', name: 'indicadorN', component: IndicadorN},
        {path: '/preguntaN', name: 'preguntaN', component: PreguntaN},
        {path: '/valoracionN', name: 'valoracionN', component: ValoracionN},
      ]
    },

  ]
})

export default router
