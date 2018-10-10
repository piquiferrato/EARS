<template>
  <div>
    <menuTecnico></menuTecnico>
    <!-- <menuUsuario></menuUsuario> -->
    <!-- <login ></login> -->
  </div>

</template>

<script>
import  login from './components/Login.vue';
import menuUsuario from './components/MenuUsuario.vue';
import menuTecnico from './components/MenuTecnico.vue';
export default {

  components: {
    login,
    menuUsuario,
    menuTecnico
  },
  data () {

    return {}
  }
}
</script>

<style>

</style>
