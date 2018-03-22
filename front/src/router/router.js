import BlogLayout from '@/components/BaseLayout/BlogLayout.vue'
import List from '@/components/Article/List.vue'
import Detail from '@/components/Article/Detail.vue'
import aboutMe from '@/components/About/aboutMe.vue'
import Page404 from '@/components/ErroPage/Page404.vue'

export const pageRouter = [
  {
    path: '/404',
    component: BlogLayout,
    children: [
      {path: '/404',name:'404',component: Page404}
    ]
  },
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
  // {
  //   path: '/news',
  //   name: 'news',
  //   redirect: '/news',
  //   component: BlogLayout, 
  // },
  {
    path: '/about',
    component: BlogLayout,
    redirect: '/about',
    children: [
      {path: '/about',name:'about',component: aboutMe}
    ]
  },
  { path: '*', redirect: '/404', hidden: true },
]

export const routers = [
  ...pageRouter,
]