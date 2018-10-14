<template>
<div>
  <div class="row backgroundColor">
    <div class="whiteText col-12">
      <a href="#" id="logOut" class="boldText whiteText ">LOGOUT</a>
      <p class="boldText text-center">BIENVENIDO "tecnico"</p>
    </div>
  </div>
  <div class="row backgroundColor">
    <div class="btn textColor btnNavigationBorder whiteBackground hover col-3 ">
      <p class="boldText text-center mt-1">PEDIDO</p>
    </div>
    <div class="btn textColor btnNavigationBorder whiteBackground hover col-3">
      <p class="boldText text-center mt-1">EN PROCESO</p>
    </div>
    <div class="btn textColor btnNavigationBorder whiteBackground hover col-3">
      <p class="boldText text-center mt-1">CANCELADO</p>
    </div>
    <div class="btn textColor btnNavigationBorder whiteBackground hover col-3">
      <p class="boldText text-center mt-1">TERMINADO</p>
    </div>
  </div>
</div>
</template>
<script>
import axios from 'axios';

export default {
  mounted(){
      axios.get('http://127.0.0.1:8000/users', {
        headers: {'Authorization': 'JWT' + sessionStorage.getItem('idToken')},
        // params: {
        //   id: this.id,
        // }
      })
      .then((response) => {
        console.log(response);
      })
      .catch((error) => {
        console.log("No salio");
      });
  },
  data: () => ({

  })
}
</script>
<style>

</style>
