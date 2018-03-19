import Vue from 'vue'
import Router from 'vue-router'
import {routers} from './router'

Vue.use(Router)

const RouterConfig = {
  mode: 'history',
  routes: routers,
  scrollBehavior (to, from, savedPosition) {
    return { x: 0, y: 0 }
  }

}

const router = new Router(RouterConfig)

export default router

// export default new Router({
//   routes: [
//     {
//       path: '/',
//       name: 'BlogLayout',
//       component: BlogLayout
//     }
//   ]
// })


