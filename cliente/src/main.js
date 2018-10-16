import Vue from 'vue';
import App from './App.vue';
import store from './store/store';
import BootstrapVue from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import router from './router/router';

Vue.use (BootstrapVue);
export const eventBus = new Vue();
new Vue({
  el: '#app',
  store,
  router,
  eventBus,
  render: h => h(App)
});
