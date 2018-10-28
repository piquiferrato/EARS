<template>
<div>
  <div class="row justify-content-center align-items-center minh-100">
    <div class="col-xs-12 boxLogin">
      <form @submit.prevent="logIn">
        <h1>BIENVENIDO</h1>
        <label class="blackText" for="username">Usuario:</label>
        <input required type="text" class="form-control" id="username" v-model="login.username">
        <label class="blackText" for="password">Contraseña</label>
        <input required type="password" class="form-control" id="password" v-model="login.password">
        <a class="blackText" id="passwordResotore" href="#">¿Haz olvidado tu contraseña?</a>
        <button type="submit" class="btnLogin btn" name="button" v-on:click="logIn">Ingregsar</button>
      </form>
    </div>
  </div>
</div>
</template>
<script>
import store from '../store/store';
import axios from 'axios';
export default {
  store,
  data: function() {
    return {
      login: {
        username: "",
        password: ""
      }
    }
  },
  methods: {
    logIn() {
      axios.post('http://127.0.0.1:8000/rest-auth/login/', {
          username: this.login.username,
          password: this.login.password
        })
        .then((data) => {
          sessionStorage.setItem('idToken', data.data.key);
          sessionStorage.setItem('idUser', data.data.user.id);
          sessionStorage.setItem('authenticate', true);
          if (data.data.user.isTechnician) {
            this.$router.push('/technicianUser');
          } else {
            this.$router.push('/user');
          }
        })
        .catch((error) => {
          this.$swal({
            type: 'error',
            title: 'Oops...',
            text: 'Tu usuario o contraseña no es correcto',
          })
          console.log(error.response);
        });
    },
  }
}
</script>
<style>
.minh-100 {
  height: 100vh;
}

.boxLogin {
  background-color: #2699FB;
  padding: 10px;
  border-radius: 15px;
  border-style: solid;
}

.btnLogin {
  margin-top: 10px;
  border-color: #000000;
  background-color: #FFFFFF;
  font-weight: bold;
  border-width: 2px;
}

.btnLogin:hover {
  border-color: #FFFFFF;
  background-color: #2699FB;
  color: #FFFFFF;
}

.blackText {
  color: #000000;
}
</style>
