<template>
<div class="container">
  <div class="row justify-content-center align-items-center minh-100">
    <div class="col-xs-12 boxLogin">
      <form>
        <h1>BIENVENIDO</h1>
        <label class="textoNegro" for="usuario">Usuario:</label>
        <input required type="text" class="form-control" id="usuario" v-model="login.usuario">
        <label class="textoNegro" for="contraseña">Contraseña</label>
        <input required type="password" class="form-control" id="contraseña"v-model="login.contraseña">
        <a class="textoNegro" id="recuperarContraseña" href="#">¿Haz olvidado tu contraseña?</a>
        <button type="submit" class="ingresar btn" name="button" v-on:click="loguear">Ingregsar</button>
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
    background-color: #2699FB;
    padding: 10px;
    border-radius: 15px;
    border-style: solid;
  }
  .ingresar {
    margin-top: 10px;
    border-color: #000000;
    background-color: #FFFFFF;
    font-weight: bold;
    border-width: 2px;
  }
  .ingresar:hover {
    border-color: #FFFFFF;
    background-color: #2699FB;
    color: #FFFFFF;
  }
  .textoNegro {
    color: #000000;
  }
</style>
