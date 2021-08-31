import Vue from 'vue';
import Router from 'vue-router';

import Body from '../components/body';
import SamplePage from '../pages/sample_page';
import Error404 from '../pages/error_404';

/* Authentication */
import login from '../auth/login';
import Register from '../auth/register';
import ResetPassword from '../auth/reset_password';


/* User Profile */
import UserProfile from '../pages/users/profile';
import UserEditProfile from '../pages/users/edit-profile';
import UserCards from '../pages/users/cards';


// component

Vue.use(Router);

const routes = [
  { path: '', redirect: { path: '/dashboard' }},
  { path: '*', redirect: { path: '/error-404' }},
  {
    path: '/dashboard',
    name: 'dashboard',
    component: Body,
    children: [
      {
        path: '',
        name: '',
        component: SamplePage,
        meta: {
          title: 'Default Dashboard | Endless - Premium Admin Template',
        }
      },
    ]
  },
  {
    path: '/login',
    name: 'login',
    component: login,
    meta: {
      title: 'Login | Endless - Premium Admin Template',
    }
  },
  {
    path: '/error-404',
    name: 'error-404',
    component: Error404,
    meta: {
      title: 'Error | Endless - Premium Admin Template',
    }
  },
  {
    path: '/register',
    name: 'register',
    component: Register,
    meta: {
      title: 'Register | Endless - Premium Admin Template',
    }
  },
  {
    path:'/resetpassword',
    name:'ResetPassword',
    component:ResetPassword,
    meta: {
      title: 'ResetPassword | Cuba - Premium Admin Template',
    }
  },
  {
    path:'/users',
    component: Body,
    children:[
      {
        path: '',
        name: '',
        component:UserCards,
        meta: {
          title: 'serCards | Cuba - Premium Admin Template',
        }
      }
    ]
  },
  {
    path:'/user',
    component: Body,
    children:[
      {
        path: 'profile',
        name: 'UserProfile',
        component:UserProfile,
        meta: {
          title: 'serProfile | Cuba - Premium Admin Template',
        }
      },
      {
        path: 'edit',
        name: 'UserEditProfile',
        component:UserEditProfile,
        meta: {
          title: 'serEditProfile | Cuba - Premium Admin Template',
        }
      },
    ]
  },
];

const router = new Router({
  routes,
  base: '/',
  mode: 'history',
  linkActiveClass: 'active',
  scrollBehavior () {
    return { x: 0, y: 0 };
  }
});

export default router;
