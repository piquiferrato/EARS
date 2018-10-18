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
    //   path: '/user',
    //   name: 'user',
    //   component: UserMenu,
    //   beforeEnter: (to, from, next) => {
    //     if (sessionStorage.getItem('authenticate') == true) {
    //       next();
    //     }else {
    //       next('/');
    //     }
    //   }
    // },
    {path: '/', component: Login},
    {path: '/user', component: UserMenu},
    {
      path: '/technicalUser',
      name: 'TechnicalMenu',
      component: TechnicalMenu
    },
  ]

});
