import BlogLayout from '@/components/BaseLayout/BlogLayout.vue'
import List from '@/components/Article/List.vue'
import Detail from '@/components/Article/Detail.vue'

export const pageRouter = [
  // {path: '/404',name: '404',component: Page404},
  {
    path: '/',
    name: 'BlogLayout',
    component: BlogLayout,
    redirect: '/blog',
    children: [
      {path: 'blog/(page/)?:page(\\d+)?/',name:'blog',component: List,alias: '/'},
      {path: 'blog/:slug',name: 'article',component: Detail}
    ]
  }
]

export const routers = [
  ...pageRouter,
]