import Vue from 'vue';
import App from './App.vue';
import store from './store/store';
import BootstrapVue from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import router from './router/router';

Vue.use (BootstrapVue);

new Vue({
  el: '#app',
  store,
  router,
  render: h => h(App)
});
