<template>
  <div>
    <!-- <menuUsuario></menuUsuario> -->
    <login ></login>
  </div>

</template>

<script>
import  login from './components/Login.vue';
import menuUsuario from './components/MenuUsuario.vue';
export default {

  components: {
    login,
    menuUsuario
  },
  data () {

    return {}
  }
}
</script>

<style>

</style>
