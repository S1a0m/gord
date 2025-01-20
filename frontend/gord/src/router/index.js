import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/:token?',
      name: 'home',
      props: true,
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/portfolio',
      name: 'portfolio',
      component: () => import('../views/PortfolioView.vue')
    },
    {
      path: '/blog',
      name: 'blog',
      component: () => import('../views/BlogView.vue')
    },
    {
      path: '/blog/:id',
      name: 'blog-lecture',
      component: () => import('../views/BlogDetailsView.vue'),
      props: true
    },
    {
      path: '/faq',
      name: 'faq',
      component: () => import('../views/FaqView.vue')
    },
    {
      path: '/projects',
      name: 'projects',
      component: () => import('../views/ProjectsView.vue')
    },
    {
      path: '/error',
      name: 'error',
      component: () => import('../views/ErrorView.vue')
    },
    // Wildcard route for undefined paths
    {
      path: '/:pathMatch(.*)*', // Matches any path not defined above
      redirect: '/error', // Redirect to error page
    },
  ],
  scrollBehavior(to, from, savedPosition) {
    if(to.hash) {
      return {
        el: to.hash,
        behavior: 'smooth',
      };
    }
    else if(savedPosition) {
      return savedPosition;
    }
    else {
      return { top: 0 };
    }
  }
})

export default router
