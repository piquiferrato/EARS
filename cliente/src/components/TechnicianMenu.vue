<template>
<div>
  <div class="row backgroundColor">
    <p class="boldText col-10">BIENVENIDO {{ name }}</p>
    <a href="#" id="logOut" class="boldText whiteText col-2" v-on:click="logOut">LOGOUT</a>
    <label class="col-2">Pedidos en espera</label>
    <label>{{ quantityOnHold }}</label>
    <label class="col-2">Pedidos en proceso</label>
    <label>{{ quantityInProcess }}</label>
    <label class="col-2">Pedidos cancelados</label>
    <label>{{ quantityCancelled }}</label>
    <label class="col-2">Pedidos resueltos</label>
    <label>{{ quantityFinished }}</label>
  </div>
  <b-navbar toggleable="md" class="row backgroundColor">
    <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
    <b-collapse is-nav id="nav_collapse">
      <b-navbar-nav class="center">
        <b-nav-item class="btn mBottom textColor btnNavigationBorder whiteBackground hover col-xs-12 col-md-4 boldText text-center mt-1" v-on:click="watch_my_requisitions_taken">MIS PEDIDOS TOMADOS</b-nav-item>
        <b-nav-item class="btn mBottom textColor btnNavigationBorder whiteBackground hover col-xs-12 col-md-4 boldText text-center mt-1" v-on:click="watch_my_requisitions_finish">MIS PEDIDOS FINALIZADOS</b-nav-item>
        <b-nav-item class="btn mBottom textColor btnNavigationBorder whiteBackground hover col-xs-12 col-md-4 boldText text-center mt-1" v-on:click="watch_all_requisitions">TODOS LOS PEDIDOS</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
  <div class="row backgroundColor" v-if="!privateSection">
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
  <technicianRequisitionTaken></technicianRequisitionTaken>
</div>
</template>
<script>
import axios from 'axios';
import techCard from './TechCard.vue'
import technicianRequisitionTaken from './TechnicianRequisitionTaken.vue'
import EventBus from '../bus/eventBus.js';
export default {
  components: {
    techCard,
    technicianRequisitionTaken
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
    this.load_quantity_requisition()
    EventBus.$on('load_quantity_requisition', () => {
      this.load_quantity_requisition()
    })
  },
  data() {
    return {
      name: null,
      onHold: true,
      inProcess: false,
      cancelled: false,
      finished: false,
      privateSection: false,
      quantityInProcess: null,
      quantityOnHold: null,
      quantityCancelled: null,
      quantityFinished: null
    }
  },
  methods: {
    load_quantity_requisition() {
      axios.get('http://127.0.0.1:8000/requisitions/status/waiting/')
        .then((response) => {
          this.quantityOnHold = response.data.length
        })
        .catch((error) => {
          console.log("No salio");
        });
      axios.get('http://127.0.0.1:8000/requisitions/status/inprogress/')
        .then((response) => {
          this.quantityInProcess = response.data.length
        })
        .catch((error) => {
          console.log("No salio");
        });
      axios.get('http://127.0.0.1:8000/requisitions/status/cancelled/')
        .then((response) => {
          this.quantityCancelled = response.data.length
        })
        .catch((error) => {
          console.log("No salio");
        });
      axios.get('http://127.0.0.1:8000/requisitions/status/done/')
        .then((response) => {
          this.quantityFinished = response.data.length
        })
        .catch((error) => {
          console.log("No salio");
        });
    },
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
    },
    watch_my_requisitions_taken() {
      EventBus.$emit('watch_my_requisitions_taken')
      this.privateSection = !this.privateSection
    },
    watch_my_requisitions_finish() {
      EventBus.$emit('watch_my_requisitions_finish')
      this.privateSection = !this.privateSection
    },
    watch_all_requisitions() {
      EventBus.$emit('watch_all_requisitions')
      this.privateSection = !this.privateSection
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
