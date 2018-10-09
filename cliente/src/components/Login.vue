<template>
<div class="container">
  <div class="row justify-content-center align-items-center minh-100">
    <div class="col-xs-12 boxLogin">
      <form>
        <h1>BIENVENIDO</h1>
        <label for="usuario">Usuario:</label>
        <input required type="text" class="form-control" id="usuario" v-model="login.usuario">
        <label for="contraseña">Contraseña</label>
        <input required type="password" class="form-control" id="contraseña"v-model="login.contraseña">
        <a id="recuperarContraseña" href="#">¿Haz olvidado tu contraseña?</a>
        <button type="submit" class="btn btn-primary" name="button" v-on:click="loguear">Ingregsar</button>
      </form>
    </div>
  </div>

</div>
</template>
<script>
import axios from 'axios'
export default {
  data() {
    return {
      login: {
        usuario: null,
        contraseña: null
      }
    }
  },
  methods: {
    loguear() {
      axios.post('', {
          username: this.username,
          password: this.password
        })
        .then((response) => {
          this.logueado = !this.logueado;
          // console.log(response);
        })
        .catch((error) => {
          // alert("usuario desconosido");
          console.log(error);
        });
    }
  }
}
</script>
<style>
  .minh-100 {
    height: 100vh;
  }
  .boxLogin {
    background-color: primary;
    padding: 10px;
    border-radius: 15px;
  }
  .btn {
    margin-top: 10px;
  }
</style>
