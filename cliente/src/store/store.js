import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user: {
      username: '',
      id: '',
      authenticated: false,
      token: ''
    }
  },
  mutations: {
    addWebToken: function(state, webToken) {
      // state.user.token = webToken;
      // sessionStorage.setItem('user', webToken);
      state.authenticated = true;
    },
    removeWebToken: function(state) {
      sessionStorage.removeItem('idToken');
      state.authenticated = false;
    }
  },
  actions: {
    logIn(context, userInPut) {
      context.commit('addWebToken', webToken);
    },
    logOut: function(context) {
      context.commit('removeWebToken');
    }
  }
});
