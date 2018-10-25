<template>
<div>
  <div class="row backgroundColor">
    <div class="whiteText col-12">
      <a href="#" id="logOut" class="boldText whiteText" v-on:click="logOut">LOGOUT</a>
      <p class="boldText text-center">BIENVENIDO {{ name }}</p>
    </div>
  </div>
  <b-navbar toggleable="md" class="row backgroundColor">
    <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
    <b-collapse is-nav id="nav_collapse">
      <b-navbar-nav class="center">
        <b-nav-item class="btn mBottom textColor btnNavigationBorder whiteBackground hover col-xs-12 col-md-6 boldText text-center mt-1">PEDIDOS TOMADOS</b-nav-item>
        <b-nav-item class="btn mBottom textColor btnNavigationBorder whiteBackground hover col-xs-12 col-md-6 boldText text-center mt-1">PEDIDOS FINALIZADOS</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>

  <div class="row backgroundColor">
    <div class="textColor btnNavigationBorder whiteBackground hover col-3" v-on:click="search_requisitions(1)" :class="{activeButton: onHold}">
      <p class="boldText text-center mt-1">EN ESPERA</p>
    </div>
    <div class="textColor btnNavigationBorder whiteBackground hover col-3" v-on:click="search_requisitions(2)" :class="{activeButton: inProcess}">
      <p class="boldText text-center mt-1">EN PROCESO</p>
    </div>
    <div class="textColor btnNavigationBorder whiteBackground hover col-3" v-on:click="search_requisitions(3)" :class="{activeButton: cancelled}">
      <p class="boldText text-center mt-1">CANCELADO</p>
    </div>
    <div class="textColor btnNavigationBorder whiteBackground hover col-3" v-on:click="search_requisitions(4)" :class="{activeButton: finished}">
      <p class="boldText text-center mt-1">TERMINADO</p>
    </div>
  </div>
  <techCard></techCard>
</div>
</template>
<script>
import axios from 'axios';
import techCard from './TechCard'
import EventBus from '../bus/eventBus.js';
export default {
  components: {
    techCard
  },
  mounted() {
    axios.get('http://127.0.0.1:8000/users/' + sessionStorage.getItem('idUser'), {
        //  params: {
        //   id: sessionStorage.getItem('idUser')
        // },
        headers: {
          'Authorization': 'JWT' + sessionStorage.getItem('idToken')
        }
      })
      .then((response) => {
        this.name = response.data.username;
      })
      .catch((error) => {
        console.log("No salio");
      });
    EventBus.$on('select_nav_btn', (status) => {
      this.correct_section(status)
    })
  },
  data() {
    return {
      name: null,
      onHold: true,
      inProcess: false,
      cancelled: false,
      finished: false,
    }
  },
  methods: {
    logOut() {
      // axios.get('http://127.0.0.1:8000/rest-auth/logout/');
      sessionStorage.clear();
      this.$router.push('/');
    },
    search_requisitions(status) {
      this.correct_section(status)
      EventBus.$emit('watch_requisition', status)
    },
    correct_section(status) {
      if (status === 1) {
        this.onHold = true
        this.inProcess = false
        this.finished = false
        this.cancelled = false
      } else if (status === 2) {
        this.onHold = false
        this.inProcess = true
        this.finished = false
        this.cancelled = false
      } else if (status === 3) {
        this.onHold = false
        this.inProcess = false
        this.finished = false
        this.cancelled = true
      } else if (status === 4) {

        this.onHold = false
        this.inProcess = false
        this.finished = true
        this.cancelled = false
      }
    }
  }
}
</script>
<style>
.activeButton {
  background: #2699FB;
  color: #FFFFFF;
  border: 1px solid #FFFFFF;
}
</style>
