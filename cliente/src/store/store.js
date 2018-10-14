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
      sessionStorage.setItem('user', webToken);
      state.authenticated = true;
    },
    removeWebToken: function(state) {
      sessionStorage.removeItem('user');
      state.authenticated = false;
      // state.user.token = '';
    }
  },
  actions: {
    loguear(context, userInPut) {
      axios.post('http://127.0.0.1:8000/rest-auth/login/', {
          username: userInPut.username,
          password: userInPut.password
        })
        .then((data) => {
          var webToken = data.data.key;
          context.commit('addWebToken', webToken);
          // router.push('/user');
          // console.log(data.data.key);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    logOut: function(context) {
      //your logout functionality
      context.commit('removeWebToken');
    }
  }
});
