import BlogLayout from '@/components/BaseLayout/BlogLayout.vue'
import List from '@/components/Article/List.vue'
import Detail from '@/components/Article/Detail.vue'
import aboutMe from '@/components/About/aboutMe.vue'

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
  },
  {
    path: '/about',
    component: BlogLayout,
    redirect: '/about',
    children: [
      {path: '/about',name:'about',component: aboutMe}
    ]
  }
]

export const routers = [
  ...pageRouter,
]