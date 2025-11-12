import { createRouter, createWebHistory } from 'vue-router'
import DashboardView from '../views/DashboardView.vue'
import UsersView from '../views/UsersView.vue'
import PostsView from '../views/PostsView.vue'
import CommentsView from '../views/CommentsView.vue'

const routes = [
  { 
    path: '/', 
    name: 'dashboard', 
    component: DashboardView 
  },
  { 
    path: '/users', 
    name: 'users', 
    component: UsersView 
  },
  { 
    path: '/posts', 
    name: 'posts', 
    component: PostsView,
    children: [
      
    ]
  },
  { 
    path: '/comments/:postId', 
    name: 'comments', 
    component: CommentsView
  } 
  
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
