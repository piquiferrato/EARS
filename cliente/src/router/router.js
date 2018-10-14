import Vue from 'vue';
import Vuex from 'vuex';
import VueRouter from 'vue-router';
import store from '../store/store';
import TechnicalMenu from '../components/TechnicalMenu';
import UserMenu from '../components/UserMenu.vue';
import Login from '../components/Login.vue';

Vue.use(VueRouter);
Vue.use(Vuex);

export default new VueRouter({
  routes: [
    // {
    //   path: '/',
    //   name: 'user',
    //   component: UserMenu,
    //   beforeEnter: (to, from, next) => {
    //     if (store.state.authenticated) {
    //       next();
    //     }else {
    //       next('/login');
    //     }
    //   }
    // },
    {path: '/', component: Login},
    {path: '/user', component: UserMenu},
    {
      path: '/techUser',
      name: 'TechnicalMenu',
      component: TechnicalMenu
    },
  ]

});
